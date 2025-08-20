from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return "No file part", 400
    file = request.files['audio']
    file.save('recording.wav')  # Save the file locally
    return "File uploaded successfully", 200

if __name__ == '__main__':
    app.run(debug=True)