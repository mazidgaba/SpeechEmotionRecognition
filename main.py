"""This is the main module to run the application."""

from predictions import make_predictions
from voice_recorder import record_audio_and_save

def main():
    try:
        choice = input("Press 'R' to record or 'P' to predict: ").strip().lower()
        
        if choice == 'r':
            # Record audio and get the saved file path
            file_path = record_audio_and_save()
            if file_path:
                # Make predictions on the recorded audio
                try:
                    predictions = make_predictions(file_path)
                    print("\nPredictions:")
                    print(f"LSTM Model predicts: {predictions['lstm_prediction']}")
                    print(f"CNN Model predicts: {predictions['cnn_prediction']}")
                except Exception as e:
                    print(f"Error making predictions: {str(e)}")
            else:
                print("Failed to record audio.")
        elif choice == 'p':
            file_path = input("Enter the path to your audio file: ").strip()
            try:
                predictions = make_predictions(file_path)
                print("\nPredictions:")
                print(f"LSTM Model predicts: {predictions['lstm_prediction']}")
                print(f"CNN Model predicts: {predictions['cnn_prediction']}")
            except Exception as e:
                print(f"Error making predictions: {str(e)}")
        else:
            print(f"Invalid choice: '{choice}'. Please enter 'R' or 'P'.")
    except EOFError:
        print("\nNo input provided. Please run the program interactively.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()