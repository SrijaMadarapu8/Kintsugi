from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import speech_recognition as sr
import os

app = Flask(__name__)
CORS(app)


def recognize_from_audio(file_path):
    r = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.record(source)  # read the entire audio file
            try:
                MyText = r.recognize_google(audio)
                MyText = MyText.lower()
                print("Did you say ", MyText)
                return MyText
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                return "Could not request results; {0}".format(e)
            except sr.UnknownValueError:
                print("Unknown error occurred")
                return "Unknown error occurred"
    except Exception as e:
        print("Error processing audio file: {0}".format(e))
        return "Error processing audio file: {0}".format(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        # Ensure the 'uploads' directory exists
        upload_dir = os.path.join(os.getcwd(), 'uploads')
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        
        # Save the file to the 'uploads' directory
        file_path = os.path.join(upload_dir, file.filename)
        file.save(file_path)
        recognized_text = recognize_from_audio(file_path)
        if recognized_text:
            return jsonify({"recognized_text": recognized_text})
        else:
            return jsonify({"error": "Could not recognize the audio"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')