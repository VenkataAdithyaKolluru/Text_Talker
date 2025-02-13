import pyttsx3

def tts(text, output_file='output.wav'):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file)
    engine.runAndWait()

# Example usage
if __name__ == "__main__":
    text = "Hello, this is a test message."
    tts(text)