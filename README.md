# YouTube Transcript API Service

A simple Flask service that fetches transcripts from YouTube videos.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Credits

This project uses the [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/) package, which provides a simple way to get transcripts/subtitles from YouTube videos. The package is maintained by Jonas Depoix and licensed under MIT License.

To learn more about the package:
- PyPI: https://pypi.org/project/youtube-transcript-api/
- GitHub: https://github.com/jdepoix/youtube-transcript-api


## Installation

1. Clone the repository:
```bash
git clone https://github.com/mppan821/youtube-transcript-api
cd youtube-transcript-api
```

2. Install required packages:
```bash
pip install flask youtube-transcript-api
```

## Usage

1. Start the server:
```bash
python3 app.py
```

The server will start on `http://localhost:5001`

2. Make a GET request to fetch transcripts:
```bash
curl "http://localhost:5001/transcript?video_id=VIDEO_ID"
```

Replace `VIDEO_ID` with the YouTube video ID (found in the video URL after `v=`)

Example:
```bash
# For video https://www.youtube.com/watch?v=dQw4w9WgXcQ
curl "http://localhost:5001/transcript?video_id=dQw4w9WgXcQ"
```

## API Reference

### GET /transcript

Fetches the transcript for a YouTube video.

**Query Parameters:**
- `video_id` (required): The YouTube video ID

**Response:**
```json
[
  {
    "text": "Transcript text",
    "start": 0.0,
    "duration": 1.5
  },
  // ... more transcript segments
]
```

**Error Response:**
```json
{
  "error": "Error message"
}
```

## Error Handling

The service returns a 400 status code with an error message if:
- The video ID is invalid
- The video doesn't have transcripts
- The transcripts are disabled for the video

## Development

To run in development mode with debug:
```bash
export FLASK_ENV=development
export FLASK_DEBUG=1
python3 transcript_service.py
```

## License

[Your License] © [Your Name]
