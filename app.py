import cv2
import numpy as np
import streamlit as st
import winsound

frequency = 2500
duration = 1000

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    st.error("Cannot open webcam")

counter = 0

st.set_page_config(
 page_title="Drowsiness Detection",
 page_icon=":sleeping:",
)

st.markdown("<h1 style='text-align: center; text-transform: uppercase; font-family: Arial, sans-serif;'>Drowsiness Detection</h1>", unsafe_allow_html=True)

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed for your safety by Falguni, Niraj, Riya and Snigdha. Drive carefully and stay safe.</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

stframe = st.empty()

while True:
    ret, frame = cap.read()
    if frame is not None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    status = "Unknown"
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Reduce minSize and increase minNeighbors for eye detection
        eyes = eyeCascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(20, 20))

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        if len(eyes) == 0:
            status = "Eyes not detected"
        else:
            status = "Open eyes"

        cv2.putText(frame, status, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    stframe.image(frame, channels="BGR")

    if status == "Eyes not detected":
        counter += 1
        if counter > 5:
            winsound.Beep(frequency, duration)
            counter = 0
    else:
        counter = 0

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
