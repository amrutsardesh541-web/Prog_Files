import cv2
import time
import threading
import sounddevice as sd
import soundfile as sf
import numpy as np
import mediapipe as mp
import librosa
import pandas as pd
import speech_recognition as sr
import whisper

# Global config
DURATION = 10  # seconds
AUDIO_PATH = 'output.wav'
VIDEO_PATH = 'output.avi'
CSV_PATH = 'session_data.csv'

# Record audio
def record_audio(path, duration):
    samplerate = 44100
    print("Recording audio...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    sf.write(path, audio, samplerate)
    print("Audio recorded and saved.")

# Capture video and extract facial, hand, and posture landmarks
def capture_video_and_landmarks(path, duration):
    cap = cv2.VideoCapture(0)
    width = int(cap.get(3))
    height = int(cap.get(4))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(path, fourcc, 20.0, (width, height))

    mp_face = mp.solutions.face_mesh
    mp_hands = mp.solutions.hands
    mp_pose = mp.solutions.pose

    face = mp_face.FaceMesh()
    hands = mp_hands.Hands()
    pose = mp_pose.Pose()

    start_time = time.time()

    print("Recording video...")
    while time.time() - start_time < duration:
        ret, frame = cap.read()
        if not ret:
            break
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_result = face.process(rgb)
        hand_result = hands.process(rgb)
        pose_result = pose.process(rgb)

        # Just overlay detected points if needed
        out.write(frame)

        cv2.imshow('Recording...', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Video recorded and saved.")

# Extract audio features
def extract_audio_features(path):
    y, sr = librosa.load(path)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    pitch = librosa.yin(y, fmin=75, fmax=300).mean()
    return {
        'pitch': pitch,
        **{f'mfcc_{i+1}': val for i, val in enumerate(mfccs.mean(axis=1))}
    }

# Transcribe speech using whisper
def transcribe_audio(path):
    print("Transcribing audio...")
    model = whisper.load_model("base")
    result = model.transcribe(path)
    print("Transcription complete.")
    return result['text']

# Save metadata to CSV
def save_to_csv(data_dict, path):
    df = pd.DataFrame([data_dict])
    df.to_csv(path, index=False)
    print(f"Data saved to {path}")

# Main application
def run_application():
    audio_thread = threading.Thread(target=record_audio, args=(AUDIO_PATH, DURATION))
    audio_thread.start()

    capture_video_and_landmarks(VIDEO_PATH, DURATION)
    audio_thread.join()

    audio_features = extract_audio_features(AUDIO_PATH)
    transcription = transcribe_audio(AUDIO_PATH)

    data = {
        'video_path': VIDEO_PATH,
        'audio_path': AUDIO_PATH,
        'transcription': transcription
    }
    data.update(audio_features)

    save_to_csv(data, CSV_PATH)

if __name__ == "__main__":
    run_application()
