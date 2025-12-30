🧠 Parkinson’s Disease Diagnosis using Spatio-Temporal Gait Analysis
(CNN–LSTM based Intelligent Medical System)
🌍 Why This Project?

Parkinson’s Disease is a progressive neurological disorder that affects movement, balance and walking patterns.
Early diagnosis is extremely important for effective treatment, but traditional diagnosis requires expensive medical equipment and continuous hospital visits.

🚑 Our goal:
To create a low-cost, non-invasive, AI-based diagnostic system that can detect Parkinson’s disease using only a walking video.

This project brings Artificial Intelligence + Healthcare together to assist doctors and patients with fast, accessible and reliable diagnosis.

✨ Uniqueness of This Project

🟢 Uses gait (walking pattern) — a powerful biological signal
🟢 Works with simple video input (no sensors, no wearables)
🟢 Extracts both:

Spatial features (how a person moves) using CNN

Temporal features (how movement changes over time) using LSTM
🟢 Provides a real-time medical web application using Streamlit
🟢 Achieved 100% test accuracy on our dataset
🟢 Built completely from scratch — dataset handling, modeling, training, deployment

🧬 What is Spatio-Temporal Gait Analysis?

🧍‍♂️ Spatial features: posture, step structure, leg motion, body alignment
⏳ Temporal features: speed, rhythm, consistency, motion sequence over time

Parkinson’s patients show clear abnormalities in both — making gait an excellent diagnostic signal.

🧠 Why CNN + LSTM?
Component	Role
CNN (Convolutional Neural Network)	Learns visual patterns from each frame
LSTM (Long Short-Term Memory)	Learns motion sequence over time

Together they form a spatio-temporal learning model — perfect for analyzing human walking.

🏗️ Complete Project Pipeline
Walking Video 🎥
        ↓
Frame Extraction (60 frames per video)
        ↓
Normalization & Sequencing
        ↓
CNN (Spatial Feature Learning)
        ↓
LSTM (Temporal Pattern Learning)
        ↓
Fully Connected Layer
        ↓
Prediction: Parkinson / Healthy
        ↓
Streamlit Web Application 🧑‍⚕️

🗂️ What We Did — Step by Step
1️⃣ Dataset Preparation

Collected 50 Parkinson + 50 Healthy walking videos

Named and organized systematically

Controlled imbalance by extracting exactly 60 frames per video

2️⃣ Frame Extraction

Uniform frame sampling

Converted all videos into equal-length gait sequences

Removed broken samples to ensure clean data

3️⃣ Data Processing

Converted frames into:

X shape: (94, 60, 128, 128, 3)
y shape: (94,)


Normalized pixel values

Assigned labels:

Parkinson → 1

Healthy → 0

4️⃣ Model Construction

CNN layers for spatial features

LSTM layer for temporal behavior

Sigmoid output for binary classification

5️⃣ Training

Train / Validation / Test split

20 training epochs

Achieved:

Training Accuracy: ~100%
Validation Accuracy: ~87% – 100%
Test Accuracy: 100%

6️⃣ Deployment

Built an interactive Streamlit medical web application

Upload a walking video → receive instant diagnosis

📊 Model Performance
Metric	Result
Training Accuracy	100%
Validation Accuracy	87% – 100%
Test Accuracy	100%
Dataset Size	94 samples
Overfitting	Controlled & minimal
🧑‍⚕️ Medical Impact

✔ Early detection
✔ Non-invasive
✔ Low-cost solution
✔ Can be used in rural & remote areas
✔ Supports clinical decision making

🚀 Technologies Used

Python 🐍

TensorFlow / Keras

OpenCV

NumPy

Streamlit

CNN–LSTM Deep Learning Architecture

🏁 Final Words

This project demonstrates how Artificial Intelligence can transform healthcare by enabling early disease detection through simple, accessible tools.
The CNN–LSTM architecture successfully learns complex human motion patterns, proving the power of spatio-temporal analysis in medical diagnosis.