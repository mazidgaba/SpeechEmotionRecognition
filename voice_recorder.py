import soundfile as sf
import sounddevice as sd
from scipy.io.wavfile import write
import os
import numpy as np

def record_audio_and_save():
    """This function records your voice and saves the output as .wav file."""
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording

    # List available audio devices and let user select one
    devices = sd.query_devices()
    print("\nAvailable audio input devices:")
    input_devices = []
    for i, device in enumerate(devices):
        if device['max_input_channels'] > 0:  # Only show input devices
            print(f"{i}: {device['name']}")
            input_devices.append(i)
            # Prefer microphone device
            if 'mic' in device['name'].lower():
                default_device = i
    
    if not input_devices:
        print("No input devices found!")
        return
    
    # Use microphone if available, otherwise first input device
    device_id = default_device if 'default_device' in locals() else input_devices[0]
    sd.default.device = device_id
    print(f"\nUsing device: {devices[device_id]['name']}")

    # Create recordings directory if it doesn't exist
    if not os.path.exists("recordings"):
        os.makedirs("recordings")

    try:
        print("\nRecording for 3 seconds... Speak now!")
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)  # Mono recording
        sd.wait()  # Wait until recording is finished
        
        # Normalize the audio data
        myrecording = np.nan_to_num(myrecording)  # Replace NaN with 0
        myrecording = np.clip(myrecording, -1.0, 1.0)  # Clip values to valid range
        
        # Save the recording
        write("recordings/myvoice.wav", fs, myrecording)
        print("Voice recording saved to recordings/myvoice.wav")
        return "recordings/myvoice.wav"
    except Exception as e:
        print(f"An error occurred while recording: {str(e)}")
        return None

if __name__ == "__main__":
    record_audio_and_save()
