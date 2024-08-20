import unittest
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

key = b'insecurekey'
iv = b'insecureiv'

def encrypt(data):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(data) + encryptor.finalize()

def decrypt(encrypted_data):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(encrypted_data) + decryptor.finalize()

class TestEncryption(unittest.TestCase):

    def test_key_length(self):
        self.assertGreaterEqual(len(key), 16, "Key length should be at least 128 bits (16 bytes)")

    def test_iv_length(self):
        self.assertEqual(len(iv), 16, "IV length should be 128 bits (16 bytes)")

    def test_encrypt_decrypt(self):
        plaintext = b'Hello, World!'
        ciphertext = encrypt(plaintext)
        decrypted_text = decrypt(ciphertext)
        
        self.assertEqual(plaintext, decrypted_text, "Encryption and decryption did not produce the same plaintext")

    def test_random_iv(self):
        iv1 = os.urandom(16)
        iv2 = os.urandom(16)

        self.assertNotEqual(iv1, iv2, "IVs should be different for each encryption")

if __name__ == '__main__':
    unittest.main()