# Voice App

This project is a simple command-line application that provides two main functionalities: Text-to-Speech (TTS) and Live Speech-to-Text (STT). Users can convert text input into speech or capture live audio and transcribe it into text.

## Features

- **Text to Speech**: Convert text input into speech and save it as an audio file.
- **Live Speech to Text**: Capture live audio input and transcribe it into text.

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd voice-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command in your terminal:

```
python src/main.py
```

You will be prompted to choose between the two functionalities:

1. Enter `1` for Text to Speech and provide the text you want to convert.
2. Enter `2` for Live Speech to Text and speak into your microphone.

## Dependencies

This project requires the following Python libraries:

- [gTTS](https://pypi.org/project/gTTS/) for text-to-speech conversion.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) for live speech recognition.
