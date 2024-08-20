import unittest
from flask import Flask, request, render_template_string
from threading import Thread
import requests

app = Flask(__name__)
app.secret_key = 'super_secret_key'
fake_db = {"user_input": ""}

class TestApp(unittest.TestCase):
    def setUp(self):
        self.server_thread = Thread(target=lambda: app.run(debug=False))
        self.server_thread.start()

    def tearDown(self):
        requests.post('http://127.0.0.1:5000/shutdown')  # Custom route to shut down the server
        self.server_thread.join()

    def start_flask_server(self):
        self.server_thread.start()

    def stop_flask_server(self):
        requests.post('http://127.0.0.1:5000/shutdown')  # Custom route to shut down the server
        self.server_thread.join()

    def test_store_route(self):
        with app.test_client() as client:
            response = client.post('/store', data={'input': 'test input'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data.decode('utf-8'), "Input stored successfully!")
            self.assertEqual(fake_db['user_input'], 'test input')

    def test_get_stored_input_route(self):
        with app.test_client() as client:
            fake_db['user_input'] = 'stored input'
            response = client.get('/get-stored-input')
            self.assertIn(b"<div>stored input</div>", response.data)

    def test_reflected_xss(self):
        with app.test_client() as client:
            payload = '<script>alert("XSS")</script>'
            response = client.get(f'/get-stored-input?input={payload}')
            self.assertNotIn(payload, response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
