import streamlit as st
import cv2
import tempfile
from plate_detection import detect_plate
from ocr import read_text

st.title("🚗 Traffic OCR System")

uploaded_file = st.file_uploader("Upload Video", type=["mp4", "avi"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    video = cv2.VideoCapture(tfile.name)

    stframe = st.empty()

    while True:
        ret, frame = video.read()
        if not ret:
            break

        frame, plates = detect_plate(frame)

        for plate in plates:
            texts = read_text(plate)
            for text in texts:
                cv2.putText(frame, text, (50,50),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0,255,0), 2)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame)

    video.release()