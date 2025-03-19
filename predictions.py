"""This module makes predictions on new voice recordings."""

import numpy as np
import joblib
from preprocessing import extract_features_single


def make_predictions(file_path):
    """
    This function takes in a file path and makes predictions on it.
    """
    # Extract features from the audio file
    features = extract_features_single(file_path)
    if features is None:
        raise Exception("Failed to extract features from the audio file")
    
    features = features.reshape(1, -1)  # Reshape for sklearn models

    try:
        # Load models
        lstm_model = joblib.load("models/lstm_model.joblib")
        cnn_model = joblib.load("models/cnn_model.joblib")
        
        # Make predictions
        lstm_pred = lstm_model.predict(features)[0]
        cnn_pred = cnn_model.predict(features)[0]

        # Define emotion labels
        emotions = ["neutral", "calm", "happy", "sad", "angry", "fearful", "disgusted", "surprised"]
        
        # Get predicted emotions
        lstm_emotion = emotions[lstm_pred]
        cnn_emotion = emotions[cnn_pred]
        
        print(f"\nThis voice sounds {lstm_emotion}")
        
        # Dictionary of emotion videos
        emotion_videos = {
            'neutral': 'https://www.youtube.com/watch?v=kRauhbZqJCY',
            'calm': 'https://www.youtube.com/watch?v=Zljg2ptExHc',
            'happy': 'https://www.youtube.com/watch?v=srYPJYgDaj8',
            'sad': 'https://www.youtube.com/watch?v=EvDQBIisG7c',
            'angry': 'https://www.youtube.com/watch?v=7D3zpOBRN9c',
            'fearful': 'https://www.youtube.com/watch?v=fcLl-DZGLZ8',
            'disgusted': 'https://www.youtube.com/watch?v=UM7ydNEK68w',
            'surprised': 'https://www.youtube.com/watch?v=JNQU-4YEnm4'
        }
        
        # Return predictions first
        result = {
            "lstm_prediction": lstm_emotion,
            "cnn_prediction": cnn_emotion
        }

        # Then handle video suggestion
        print("\nDo you want to see a video matching your emotion?")
        try:
            choice = input('Type YES or NO in capital: ')
            if choice == 'YES':
                import webbrowser
                print("\nWait! We are searching for a video matching your emotion!")
                url = emotion_videos.get(lstm_emotion, emotion_videos['neutral'])
                
                try:
                    webbrowser.register('chrome', None,
                        webbrowser.BackgroundBrowser("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"))
                    webbrowser.get('chrome').open(url)
                except Exception as e:
                    print(f"Could not open browser: {str(e)}")
                    print(f"You can manually visit: {url}")
            else:
                print("Ok, bye!")
        except EOFError:
            print("\nCould not read input for video choice. Skipping video suggestion.")
        except Exception as e:
            print(f"\nError handling video suggestion: {str(e)}")
        
        return result
        
    except Exception as e:
        print(f"Error making predictions: {str(e)}")
        return {
            "lstm_prediction": "error",
            "cnn_prediction": "error"
        }

if __name__ == "__main__":
    work_rec = "recordings/findahappyplace.wav"
    predictions = make_predictions(file_path=work_rec)
    print("\nPredictions:")
    print(f"LSTM Model predicts: {predictions['lstm_prediction']}")
    print(f"CNN Model predicts: {predictions['cnn_prediction']}")