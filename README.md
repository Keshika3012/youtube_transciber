# YouTube Transcriber - AI Powered Tutor

An intelligent YouTube video transcriber that extracts transcripts from YouTube videos and allows users to ask questions about the content using AI.

## Features

- Extract transcripts from YouTube videos with English captions
- AI-powered question answering using OpenAI GPT models
- Vector-based document retrieval using FAISS
- Clean, interactive web interface built with Streamlit

## Requirements

- Python 3.9+
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Youtube_transcripter
```

2. Create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Enter a YouTube video URL with English captions

4. Click "process video" to extract and analyze the transcript

5. Ask questions about the video content in the question input field

## Dependencies

- streamlit
- langchain-community
- openai
- faiss-cpu
- tiktoken
- youtube-transcript-api
- pytube
- python-dotenv

## Notes

- Only works with YouTube videos that have English transcripts/captions available
- Requires a valid OpenAI API key for AI-powered Q&A functionality
- The app creates temporary transcript files that are automatically processed

## License

MIT License
