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

import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import imagehash

def audio_to_spectrogram(audio_path):
    """ Convert an audio file into a spectrogram image """
    y, sr = librosa.load(audio_path, sr=None)
    spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
    log_spectrogram = librosa.power_to_db(spectrogram, ref=np.max)

    # Save as image
    plt.figure(figsize=(4, 4))
    librosa.display.specshow(log_spectrogram, sr=sr, x_axis='time', y_axis='mel')
    plt.axis('off')
    plt.savefig("spectrogram.png", bbox_inches='tight', pad_inches=0)
    plt.close()

    return "spectrogram.png"

def get_perceptual_hash(image_path):
    """ Compute perceptual hash from the spectrogram image """
    img = Image.open(image_path).convert("L")  # Convert to grayscale
    return imagehash.phash(img)  # Perceptual Hashing

# Example Usage
audio_file_1 = "audio1.wav"  # First audio file
audio_file_2 = "audio2.wav"  # Slightly modified version

# Convert to spectrograms and hash them
spectrogram_1 = audio_to_spectrogram(audio_file_1)
spectrogram_2 = audio_to_spectrogram(audio_file_2)

hash1 = get_perceptual_hash(spectrogram_1)
hash2 = get_perceptual_hash(spectrogram_2)

# Print Hashes
print(f"Hash 1: {hash1}")
print(f"Hash 2: {hash2}")

# Compare Hash Similarity
hamming_distance = hash1 - hash2
print(f"Hamming Distance: {hamming_distance}")

