from flask import Flask, request, send_file, jsonify
from gtts import gTTS
import os
from io import BytesIO

# Initialize the Flask app
app = Flask(__name__)

@app.route('/text-to-speech', methods=['POST'])
def convert_text_to_speech():
    try:
        # Get the data from the request
        data = request.get_json()
        text = data.get('text')
        language = data.get('language', 'en')  # Default to 'en' if language is not provided

        # Validate the input
        if not text:
            return jsonify({'error': 'Text is required'}), 400
        
        # Convert text to speech
        tts = gTTS(text=text, lang=language, slow=False)

        # Save to a file-like object (BytesIO)
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)  # Reset file pointer to the beginning

        # Return the mp3 file as a response
        return send_file(mp3_fp, mimetype="audio/mpeg", as_attachment=True, download_name="output.mp3")
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='192.168.1.30', port=5000, debug=True)

