import librosa
import numpy as np

# Load and generate spectrogram
y, sr = librosa.load("01. Supremacy.mp3")
S = librosa.feature.melspectrogram(y=y, sr=sr)
S_db = librosa.power_to_db(S, ref=np.max)

# Normalize and map to ASCII characters
chars = "@%#*+=-:. "
scaled = (S_db - np.min(S_db)) / (np.max(S_db) - np.min(S_db))  # Normalize between 0-1
ascii_art = "\n".join(["".join([chars[int(v * (len(chars) - 1))] for v in row]) for row in scaled])
import base64
import zlib
compressed_data = base64.b85encode(ascii_art.encode()).decode()
compressed_zlib = zlib.compress(ascii_art.encode())
