# Text-to-Speech API

This repository contains a Flask-based API that converts text to speech using Google Text-to-Speech (gTTS) and returns the audio file as an MP3 file without saving it to the disk.

## How It Works

The API takes input text and an optional language code, converts the text to speech, and returns an MP3 audio file as a response. The file is returned directly as an attachment in memory without saving it on the server.

## Prerequisites

Before running the project, ensure that you have the following installed:

- **Python 3.6+**
- **Flask** (Python web framework)
- **gTTS** (Google Text-to-Speech library)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## API Endpoint

### `POST /text-to-speech`

This endpoint converts text to speech and returns an MP3 audio file.

#### Request

- **Method**: `POST`
- **Endpoint**: `/text-to-speech`
- **Headers**: `Content-Type: application/json`
- **Body**:
    - `text`: (string) The text you want to convert to speech. This is a required parameter.
    - `language`: (string) The language code for speech synthesis (optional, defaults to `en`).

#### Example Request

```bash
curl -X POST http://192.168.1.30:5000/text-to-speech \
-H "Content-Type: application/json" \
-d '{
  "text": "Hello, welcome to the text to speech conversion.",
  "language": "en"
}'
```

## Example JSON Body

```json
{
  "text": "Hello, welcome to the text to speech conversion.",
  "language": "en"
}
```

## Response

- **File**: MP3 file returned as an attachment.
- **MIME Type**: `audio/mpeg`

On successful request, an MP3 file will be returned as a downloadable attachment.

### Example Response

The response will be an MP3 file attachment (e.g., `audio_20241009152345.mp3`).

## Running the Application

To run the Flask application, use the following command:

```bash
python app.py
```