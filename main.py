from tts import tts
from stt import live_stt

def text_to_speech():
    text = input("Enter the text you want to convert to speech: ")
    tts(text)
    print("Speech has been saved to 'output.wav'.")

def live_speech_to_text():
    try:
        transcription = live_stt()
        if transcription:
            print("Transcription:", transcription)
        else:
            print("No transcription available.")
    except Exception as e:
        print(f"An error occurred during live speech recognition: {e}")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Text to Speech")
    print("2. Live Speech to Text")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        text_to_speech()
    elif choice == '2':
        live_speech_to_text()
    else:
        print("Invalid choice. Please enter 1 or 2.")