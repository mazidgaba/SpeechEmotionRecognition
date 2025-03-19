Here's the content for your README file:

# Speech Emotion Recognition System

A deep learning-based system that recognizes emotions from speech using LSTM and CNN models. Features real-time voice recording, emotion analysis, and support for pre-recorded audio files. Classifies seven emotions (happy, sad, angry, neutral, fearful, disgust, surprised) using advanced audio features like MFCC, spectrograms, and chroma features.

## Quick Start
```bash
git clone https://github.com/yourusername/speech_emotion_recognition.git
cd speech_emotion_recognition
python -m venv .venv
.\.venv\Scripts\activate  # Windows
pip install -r requirements.txt
python main.py
```

### Usage
- Press 'R' to record and analyze voice
- Press 'P' to analyze existing audio file

## Features
- Real-time voice recording and emotion analysis
- Support for pre-recorded audio file analysis
- Dual model architecture (LSTM and CNN)
- Comprehensive feature extraction:
  - MFCC (Mel-frequency cepstral coefficients)
  - Spectrograms
  - Chroma features
  - Statistical measures
- Emotion classification into seven categories
- User-friendly command-line interface
- Real-time processing capabilities

## Technologies Used
- Python 3.8+
- PyTorch
- librosa
- scikit-learn
- numpy
- pandas
- sounddevice
- soundfile

## Project Structure
```
speech_emotion_recognition/
├── datasets/              # Dataset storage
├── features/             # Extracted features
├── models/               # Trained models
├── recordings/           # Audio recordings
├── main.py              # Main application entry
├── models.py            # Model definitions
├── predictions.py       # Prediction logic
├── preprocessing.py     # Data preprocessing
├── voice_recorder.py    # Audio recording
└── requirements.txt     # Dependencies
```

## Author
Gulam Mazid | B.Tech Computer Science | Maulana Azad National Urdu University

Made with ❤️
