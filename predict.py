import librosa
import numpy as np
import tensorflow as tf
import pickle

# Load trained models
rf_model = pickle.load(open("models/random_forest.pkl", "rb"))
cnn_model = tf.keras.models.load_model("models/cnn_model.h5")

# Load label encoder
encoder = pickle.load(open("models/label_encoder.pkl", "rb"))

def load_audio_features(file_path):
    y, sr = librosa.load(file_path, sr=22050, duration=5)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfccs, axis=1).reshape(1, -1)

def predict_genre_rf(audio_path):
    feature = load_audio_features(audio_path)
    prediction = rf_model.predict(feature)
    genre = encoder.inverse_transform(prediction)[0]
    print(f"🎵 Predicted Genre (Random Forest): {genre}")
    return genre
