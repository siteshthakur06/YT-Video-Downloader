import yt_dlp
from flask import Flask, request, jsonify
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  
@app.route('/download', methods=['POST'])

def download_video():
    try:
        data = request.json
        url = data.get('url')

        if not url:
            return jsonify({"error": "No URL provided"}), 400

        options = {
            'format': 'best',
            'outtmpl': '/downloads/%(title)s.%(ext)s'
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        return jsonify({"message": "Download successful! Video saved in the downloads folder."})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "Backend is running!"
    
if __name__ == "__main__":
    app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port)
