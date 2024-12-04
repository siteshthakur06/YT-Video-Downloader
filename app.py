import yt_dlp
from flask import Flask, request, jsonify
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  
@app.route('/download', methods=['POST'])

def download_video():
    try:
        # Get the URL from the incoming request
        data = request.json
        url = data.get('url')

        if not url:
            return jsonify({"error": "No URL provided"}), 400

        # yt-dlp options
        options = {
            'format': 'best',
            'outtmpl': './downloads/%(title)s.%(ext)s'  # Save file to the 'downloads' folder
        }

        # Download the video
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        return jsonify({"message": "Download successful! Video saved in the downloads folder."})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)