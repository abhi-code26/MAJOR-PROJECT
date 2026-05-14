import streamlit as st
import cv2
import tempfile
from ultralytics import YOLO

st.title("🚗 AI Traffic Monitoring System")

option = st.selectbox(
    "Choose Input",
    ["Upload Video", "Use Webcam"]
)

model = YOLO("yolov8n.pt")

if option == "Upload Video":

    video_file = st.file_uploader("Upload Traffic Video")

    if video_file is not None:

        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(video_file.read())

        cap = cv2.VideoCapture(tfile.name)

        stframe = st.empty()

        while cap.isOpened():

            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame)

            annotated = results[0].plot()

            stframe.image(annotated, channels="BGR")

        cap.release()


if option == "Use Webcam":

    run = st.button("Start Camera")

    if run:

        cap = cv2.VideoCapture(0)

        stframe = st.empty()

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            results = model(frame)

            annotated = results[0].plot()

            stframe.image(annotated, channels="BGR")

        cap.release()
