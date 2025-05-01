from flask import Flask, render_template, request, flash, redirect, url_for
import re
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)
app.secret_key = 'Super_secret_key'  # Required for flash messages

def extract_video_id(url):
    """Extract YouTube video ID from a URL."""
    # Regular expression for YouTube URLs
    youtube_regex = (
        r'(https?://)?(www\.)?'
        r'(youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)'
        r'([a-zA-Z0-9_-]{11})'
    )
    match = re.match(youtube_regex, url)
    if match:
        return match.group(4)  # Return the video ID
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    video_id = None
    if request.method == 'POST':
        youtube_url = request.form.get('youtube_url')
        if not youtube_url:
            flash('Please provide a YouTube URL.')
            return redirect(url_for('index'))
        
        video_id = extract_video_id(youtube_url)
        if not video_id:
            flash('Invalid YouTube URL. Please provide a valid YouTube video link.')
            return redirect(url_for('index'))
    
    return render_template('index.html', video_id=video_id)

if __name__ == '__main__':
    app.run(debug=True)
