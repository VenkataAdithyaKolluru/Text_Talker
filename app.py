from flask import Flask, render_template, request, redirect, url_for
from tts import tts
from stt import live_stt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    text = request.form['text']
    tts(text)
    return redirect(url_for('index'))

@app.route('/live-speech-to-text', methods=['POST'])
def live_speech_to_text():
    transcription = live_stt()
    return render_template('index.html', transcription=transcription)

if __name__ == '__main__':
    app.run(debug=True)