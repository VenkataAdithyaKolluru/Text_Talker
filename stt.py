import speech_recognition as sr

def live_stt(timeout=10):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak now...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        try:
            audio = recognizer.listen(source, timeout=timeout)
        except sr.WaitTimeoutError:
            return "Listening timed out while waiting for phrase to start"
    
    try:
        # Use Google's Web Speech API
        transcription = recognizer.recognize_google(audio)
        return transcription
    except sr.UnknownValueError:
        return "Google Web Speech API could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Web Speech API; {e}"

# Example usage
if __name__ == "__main__":
    transcription = live_stt(timeout=10)  # Decreased timeout to 10 seconds
    print("Transcription:", transcription)