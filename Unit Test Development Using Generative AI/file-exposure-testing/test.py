import unittest
import threading
import requests

from flask import Flask
from your_file import files, upload_file

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/files/<path:filename>', 'files', files)
        self.app.add_url_rule('/upload', 'upload_file', upload_file, methods=['POST'])

        self.server_thread = threading.Thread(target=self.app.run, kwargs={'debug': False})
        self.server_thread.start()

    def tearDown(self):
        self.app.do_teardown()
        self.server_thread.join()

    def test_path_traversal_vulnerability(self):
        response = requests.get('http://127.0.0.1:5000/files/../run.py')
        # Check if the response contains part of the source code
        self.assertIn("from flask import Flask, send_from_directory, request", response.content)

    def test_direct_file_access_vulnerability(self):
        response = requests.get('http://127.0.0.1:5000/files/sensitive_file.txt')
        # Check if the response contains sensitive data
        self.assertIn("Sensitive Data", response.content)

    def test_file_upload_vulnerability(self):
        files = {'file': open('test_file.txt', 'rb')}
        response = requests.post('http://127.0.0.1:5000/upload', files=files)
        self.assertEqual(response.text, "File uploaded successfully!")
        
        # Check if the uploaded file can be accessed
        response = requests.get('http://127.0.0.1:5000/files/test_file.txt')
        self.assertEqual(response.status_code, 200)

    def test_protected_files_access(self):
        response = requests.get('http://127.0.0.1:5000/files/protected_file.txt')
        # Check if the response contains protected file data
        self.assertIn("Protected Data", response.content)

if __name__ == '__main__':
    unittest.main()