import unittest
import requests
import threading
from flask import Flask

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.server_thread = threading.Thread(target=app.run, kwargs={'debug': False})
        self.server_thread.start()

    def tearDown(self):
        requests.get('http://127.0.0.1:5000/shutdown')
        self.server_thread.join()

    def test_admin_access(self):
        # Test admin access to admin panel
        with requests.Session() as session:
            response = session.post('http://127.0.0.1:5000/login', data={'username': 'admin', 'password': 'adminpass'})
            self.assertEqual(response.status_code, 302)  # Redirect expected
            response = session.get('http://127.0.0.1:5000/admin')
            self.assertEqual(response.text, 'Admin Panel - only for admins')

    def test_user_access(self):
        # Test non-admin access to admin panel
        with requests.Session() as session:
            response = session.post('http://127.0.0.1:5000/login', data={'username': 'user', 'password': 'userpass'})
            self.assertEqual(response.status_code, 302)  # Redirect expected
            response = session.get('http://127.0.0.1:5000/admin')
            self.assertEqual(response.url, 'http://127.0.0.1:5000/')  # Redirected to index

    def test_logout_admin(self):
        # Test admin access after logout
        with requests.Session() as session:
            response = session.post('http://127.0.0.1:5000/login', data={'username': 'admin', 'password': 'adminpass'})
            self.assertEqual(response.status_code, 302)  # Redirect expected
            session.get('http://127.0.0.1:5000/logout')
            response = session.get('http://127.0.0.1:5000/admin')
            self.assertEqual(response.url, 'http://127.0.0.1:5000/')  # Redirected to index

if __name__ == '__main__':
    unittest.main()