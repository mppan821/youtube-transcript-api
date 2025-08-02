from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route("/transcript", methods=["GET"])
def transcript():
    video_id = request.args.get("video_id")
    try:
        transcript_api = YouTubeTranscriptApi()
        transcript = transcript_api.fetch(video_id)
        return jsonify(transcript)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(port=5001)
