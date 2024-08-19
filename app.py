from flask import Flask, render_template, request, redirect, url_for, flash
from pytube import YouTube
import yt_dlp

app = Flask(__name__)
app.secret_key = 'your_secret_key'


def download_video(url, path="downloads/"):
    ydl_opts = {
        'outtmpl': f'{path}/%(title)s.%(ext)s',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return "Download complete"
    except Exception as e:
        return f"Error: {str(e)}"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = url = request.form['url'].strip() 
    message = download_video(url) 
    flash(message) 
    return redirect(url_for('index'))  # Redirect back to the homepage

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
