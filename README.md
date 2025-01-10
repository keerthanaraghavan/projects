**Face Recognition Using TensorFlow and OpenCV**

**Features**

Real-time Recognition: Detects and classifies faces in real-time using a webcam.

Customizable Classes: Allows users to define and train classes for recognition.

Simple Workflow: Easy-to-follow procedure with Google Teachable Machine for training and TensorFlow for inference.

High Accuracy: Confidence scores provide insights into the reliability of predictions.

Lightweight Setup: Requires minimal dependencies and runs on a standard computer with a webcam.

Extensible: Can be adapted for object recognition, gesture detection, or other classification tasks.


**Full Project Procedure**

This section provides a step-by-step guide to building a face recognition system using Google Teachable Machine, TensorFlow, and OpenCV.


**Step 1: Collect and Train Data Using Teachable Machine**

**Go to Teachable Machine**
![Screenshot (32)](https://github.com/user-attachments/assets/51f70daa-f630-4440-a720-4813cd1bef77)


Open the Teachable Machine website.

Choose a Project Type

**Select "Image Project**."

![Screenshot (33)](https://github.com/user-attachments/assets/3dc3d369-a1be-473d-b1af-75336a88e5bc)

Add Classes

Add a class for each person or object you want to recognize. For example, "Person A," "Person B," etc.

Collect Training Data

Use your webcam or upload images for each class. Ensure you collect diverse and well-lit images for accurate training.

**Train the Model**

**Click "Train Model" to train the image recognition model**.
![WhatsApp Image 2025-01-09 at 10 42 20 PM](https://github.com/user-attachments/assets/ea9e06ce-fc1c-482a-8e4f-755cb9851173)


**Export the Model**

**Once training is complete, export the model**.

**Select the TensorFlow Lite or Keras format and download the model files (keras_model.h5 and labels.txt).**

**Step 2: Set Up the Project Environmen**t

**Install Python**

Download and install Python 3.12 from the official Python website.

Install Required Libraries

Open a terminal or command prompt and run:

**pip install tensorflow opencv-python numpy**

Create a Project Folder

Organize your files into a folder. Place keras_model.h5, labels.txt, and the Python script (main.py) in the same directory.

**Step 3: Write the Python Script**

**Import Required Libraries**

from tensorflow.keras.models import load_model
import cv2
import numpy as np

**Load the Model and Labels**

model = load_model("keras_model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()

Capture Webcam Feed and Predict

camera = cv2.VideoCapture(0)
while True:
    ret, image = camera.read()
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    image = (image / 127.5) - 1
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    print("Class:", class_name.strip(), "Confidence Score:", confidence_score)
    if cv2.waitKey(1) == 27:  # ESC key
        break
camera.release()
cv2.destroyAllWindows()


**Step 4: Run the Project**

**Start the Script**

**Run the Python script:**
The webcam feed will open. You will see predictions and confidence scores in the terminal.
![Screenshot (37)](https://github.com/user-attachments/assets/9eb6ee17-62c7-47b7-babf-8ad05e58d10d)



**python main.py**
View Predictions

![image](https://github.com/user-attachments/assets/491bb268-a217-4ff2-8b20-1df4f7001ab8)




Exit the Program

Press the ESC key to close the webcam feed.

Notes for Improvement

Ensure your training data is diverse and representative.

Adjust the model and preprocessing code as needed for better accuracy.

Use a higher-quality camera if available for better recognition.

**License**

This project is for educational purposes. Feel free to use and modify it as needed.

