# **Drowsiness Detection System**

## **Problem Statement**
The "Drowsiness Detection System" addresses the critical issue of drowsiness while driving, which can lead to serious accidents and fatalities. Current drowsiness detection methods often require complex equipment, but this web app provides a simple, accessible solution using a basic webcam and computer vision algorithms. This enables drivers to monitor their drowsiness levels and take action to prevent accidents.

## **Introduction**
The "Drowsiness Detection" web app is designed to detect driver drowsiness using a webcam. By leveraging Haar Cascades for face and eye detection, the app can determine if a driver's eyes are closed and sound an alarm if drowsiness is detected. The user interface, built with Streamlit, is intuitive and easy to use, requiring only a working webcam and an internet connection.

## **Key Features**
- Real-time drowsiness detection while driving.
- Computer vision-based detection of closed or open eyes.
- Alarm sounds if the driver's eyes are closed for an extended period.
- Helps prevent accidents caused by driver fatigue.
- Visual display of the driver's face with bounding boxes around the eyes and face.
- Accessible through a web-based interface.

## **Diagram**
![Diagram](https://github.com/nir25aj/Drowsiness_Detection_System/blob/main/App_Flow.png "Diagram")

## **Technologies Used**
- **OpenCV**
- **Streamlit**
- **Haar Cascade Classifier**
- **Winsound**

## **Methodologies**
- **Computer Vision:** Utilizes OpenCV for real-time face and eye detection using Haar cascades.
- **User Interface:** Streamlit library for rapid prototyping and user-friendly interface design.
- **Image Processing:** NumPy for tasks such as converting images from BGR to grayscale.
- **Sound Alerts:** Winsound library to produce alert sounds when the driver's eyes remain closed for more than 5 frames.

## ** Application's Interface**
![Open Eyes](https://github.com/nir25aj/Drowsiness_Detection_System/blob/main/Open_Eyes_Demonstaration.png "Open Eyes")
![Closed Eyes](https://github.com/nir25aj/Drowsiness_Detection_System/blob/main/Closed_Eyes_Demonstaration.png "Closed Eyes")
