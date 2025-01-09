import cv2
import numpy as np
from keras.models import load_model
import psycopg2
from datetime import datetime
import time

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# Connect to PostgreSQL database
try:
    conn = psycopg2.connect(
        host="localhost",
        user="postgres",  # Change to your PostgreSQL username
        password="keerthy",  # Change to your PostgreSQL password
        database="attendance"  # Change to your database name
    )
    cursor = conn.cursor()
    print("Database connection established.")
except Exception as e:
    print(f"Error connecting to database: {e}")
    exit()

# CAMERA settings
camera = cv2.VideoCapture(0)

# Helper function to mark attendance
def mark_attendance(person_name):
    current_date = datetime.now().strftime('%Y-%m-%d')  # Get today's date
    current_time = datetime.now().strftime('%H:%M:%S')  # Get current time

    try:
        # Fetch regno from the Persons table
        cursor.execute("SELECT regno FROM Persons WHERE name = %s", (person_name,))
        regno_record = cursor.fetchone()

        if not regno_record:
            print(f"Error: {person_name} not found in the database.")
            return

        regno = regno_record[0]
        print(f"Found regno for {person_name}: {regno}")

        # Check if the person has already been marked for today
        cursor.execute("SELECT * FROM Attendance WHERE person_name = %s AND date = %s", (person_name, current_date))
        record = cursor.fetchone()

        if record:
            print(f"Attendance for {person_name} already marked today.")
        else:
            # Insert attendance into the Attendance table
            cursor.execute("""
                INSERT INTO Attendance (person_name, regno, date, time)
                VALUES (%s, %s, %s, %s)
            """, (person_name, regno, current_date, current_time))
            conn.commit()  # Commit the changes

            # Update attendance count in the Persons table
            cursor.execute("""
                UPDATE Persons
                SET attendance = attendance + 1
                WHERE regno = %s
            """, (regno,))
            conn.commit()

            print(f"Attendance marked for {person_name} at {current_time}")
    except Exception as e:
        conn.rollback()  # Rollback any changes if an error occurs
        print(f"Error marking attendance: {e}")

# Initialize attendance tracking variables
last_detected_person = ""
last_detection_time = time.time()  # Track last detection time

while True:
    # Grab the webcam image
    ret, image = camera.read()

    if not ret:
        print("Failed to grab image.")
        break

    # Resize image to match model input
    image_resized = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    cv2.imshow("Webcam Image", image)

    # Prepare the image for prediction
    image_array = np.asarray(image_resized, dtype=np.float32).reshape(1, 224, 224, 3)
    image_array = (image_array / 127.5) - 1  # Normalize image

    # Get predictions (with verbose=0)
    prediction = model.predict(image_array, verbose=0)
    index = np.argmax(prediction)
    class_name = " ".join(class_names[index].strip().split(" ")[1:])

    confidence_score = prediction[0][index]
    print(f"Prediction: {class_name}, Confidence: {confidence_score * 100:.2f}%")

    # If confidence is above 90%, mark attendance
    if confidence_score > 0.90:
        if class_name != last_detected_person:
            print(f"Detected: {class_name}, Confidence: {confidence_score * 100:.2f}%")
            mark_attendance(class_name)
            last_detected_person = class_name
            last_detection_time = time.time()  # Update the last detection time
        elif time.time() - last_detection_time > 5:
            print(f"{class_name} is already in front of the camera.")
            last_detection_time = time.time()  # Reset detection timer
    elif confidence_score < 0.25:
        # Reset if person moves out of camera frame
        last_detected_person = ""
        print("No person detected with significant confidence (< 25%)")

    # Listen to the keyboard for presses (press ESC to exit)
    keyboard_input = cv2.waitKey(1)

    if keyboard_input == 27:  # ESC key to quit
        break

# Release resources and close window
camera.release()
cv2.destroyAllWindows()

# Close database connection
cursor.close()
conn.close()
