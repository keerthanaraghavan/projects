**Face Recognition Using TensorFlow and OpenCV**

**Features**
Real-time Recognition: Detects and classifies faces in real-time using a webcam.
Customizable Classes: Allows users to define and train classes for recognition.
Simple Workflow: Easy-to-follow procedure with Google Teachable Machine for training and TensorFlow for inference.
High Accuracy: Confidence scores provide insights into the reliability of predictions.
Lightweight Setup: Requires minimal dependencies and runs on a standard computer with a webcam.
Extensible: Can be adapted for object recognition, gesture detection, or other classification tasks.

**Full Project Procedure**
This guide outlines the steps to build a face recognition system using Google Teachable Machine, TensorFlow, and OpenCV.

**Step 1: Collect and Train Data Using Teachable Machine**
Go to Teachable Machine
![Screenshot (32)](https://github.com/user-attachments/assets/51f70daa-f630-4440-a720-4813cd1bef77)

Open the Teachable Machine website.
Choose a Project Type

**Select the "Image Project" option.**
![Screenshot (33)](https://github.com/user-attachments/assets/3dc3d369-a1be-473d-b1af-75336a88e5bc)
Add Classes

Define a class for each person or object you want to recognize.
For example: "Person A," "Person B," etc.
Collect Training Data

Use your webcam or upload images for each class.
Ensure the images are well-lit and diverse for better accuracy.
Train the Model

**Click the "Train Model" button to start training**.
![WhatsApp Image 2025-01-09 at 10 42 20 PM](https://github.com/user-attachments/assets/ea9e06ce-fc1c-482a-8e4f-755cb9851173)
Export the Model

After training, export the model in TensorFlow Lite or Keras format.
Download the model files: keras_model.h5 and labels.txt.

**Step 2: Set Up the Project Environment**
Install Python

Download and install Python 3.12 from the official Python website.
Install Required Libraries

Use the following command to install required libraries:
bash
Copy code
**pip install tensorflow opencv-python numpy**
Create a Project Folder

Create a folder to organize your files.
**Add the following files to the folder**:
keras_model.h5 (trained model)
labels.txt (class labels)
main.py (Python script for running the program).

**Step 3: Run the Project**
![Screenshot (44)](https://github.com/user-attachments/assets/7e56bb39-268e-4a3a-8350-79f48f99f27e)


Start the Program

**Run the Python script (image.py).**
![Screenshot (37)](https://github.com/user-attachments/assets/9eb6ee17-62c7-47b7-babf-8ad05e58d10d)

**View Predictions**
![image](https://github.com/user-attachments/assets/491bb268-a217-4ff2-8b20-1df4f7001ab8)
The webcam feed will open, and predictions with confidence scores will be displayed in the terminal.
Exit the Program

Press the ESC key to close the webcam feed.

**Notes for Improvement**
Training Data: Ensure your training data is diverse and includes variations in lighting, angles, and backgrounds.
Model Accuracy: Modify and fine-tune the preprocessing code if needed to improve accuracy.
Camera Quality: Use a higher-resolution webcam for better detection and recognition.

**Troubleshooting**
- **Issue**: Model not loading or files missing.  
  **Fix**: Ensure `keras_model.h5` and `labels.txt` are in the same directory as the Python script.  
- **Issue**: Webcam not working.  
  **Fix**: Check if the camera is connected or accessible by the system.  


**License**
This project is designed for educational purposes. Feel free to use, modify, and adapt it as needed.
