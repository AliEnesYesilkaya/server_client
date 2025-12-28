import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class RSACipher:

    def generate_keys(self):
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        return private_key, public_key

    def encrypt(self, text, public_key_bytes):
        public_key = RSA.import_key(public_key_bytes)
        cipher = PKCS1_OAEP.new(public_key)
        encrypted = cipher.encrypt(text.encode())
        return base64.b64encode(encrypted).decode()

    def decrypt(self, text, private_key_bytes):
        private_key = RSA.import_key(private_key_bytes)
        cipher = PKCS1_OAEP.new(private_key)
        decrypted = cipher.decrypt(base64.b64decode(text))
        return decrypted.decode()
