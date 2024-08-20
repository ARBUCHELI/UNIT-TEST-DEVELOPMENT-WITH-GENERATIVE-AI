from flask import Flask, send_from_directory, request

app = Flask(__name__)

@app.route('/files/', methods=['GET'])
def files(filename):
    # Insecure file serving - vulnerable to path traversal attacks.
    return send_from_directory('files', filename)

@app.route('/upload', methods=['POST'])
def upload_file():
    # File upload without proper validation can lead to sensitive file exposure.
    file = request.files['file']
    file.save(f"./uploaded_files/{file.filename}")
    return "File uploaded successfully!"

if __name__ == '__main__':
    app.run(debug=True)