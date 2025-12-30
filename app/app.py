import streamlit as st
import tensorflow as tf
import cv2
import numpy as np
import tempfile
import os

MODEL_PATH = "model/parkinson_cnn_lstm.h5"
IMG_SIZE = 128
SEQUENCE_LENGTH = 60

model = tf.keras.models.load_model(MODEL_PATH)

st.set_page_config(page_title="Parkinson's Gait Diagnosis", layout="centered")

st.title("🧠 Parkinson's Disease Diagnosis using Gait Analysis")
st.markdown("Upload a gait walking video and get instant medical prediction.")

uploaded_video = st.file_uploader("Upload Gait Video", type=["mp4", "avi"])

def extract_60_frames_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    indices = np.linspace(0, total_frames - 1, SEQUENCE_LENGTH, dtype=int)

    frames = []
    count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if count in indices:
            frame = cv2.resize(frame, (IMG_SIZE, IMG_SIZE))
            frame = frame / 255.0
            frames.append(frame)

        count += 1

    cap.release()
    return np.array(frames)

if uploaded_video:
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(uploaded_video.read())
        video_path = temp.name

    st.video(uploaded_video)

    frames = extract_60_frames_from_video(video_path)

    if len(frames) != SEQUENCE_LENGTH:
        st.error("Video is too short for analysis.")
    else:
        frames = np.expand_dims(frames, axis=0)
        prediction = model.predict(frames)[0][0]

        if prediction > 0.5:
            st.error("🧬 Parkinson's Disease Detected")
        else:
            st.success("💚 Healthy Gait Detected")

    os.remove(video_path)
