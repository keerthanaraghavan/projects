import cv2

# Initialize webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Unable to access webcam.")
else:
    print("Webcam is accessible.")

while True:
    ret, frame = camera.read()
    if not ret:
        print("Failed to capture image.")
        break

    # Display the webcam feed
    cv2.imshow("Webcam Feed", frame)

    # Exit loop if ESC key is pressed
    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        print("ESC pressed, closing webcam.")
        break

camera.release()
cv2.destroyAllWindows()
