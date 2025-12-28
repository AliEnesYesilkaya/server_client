import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from kripto.cipher_base import CipherAlgorithm


class AESCipher(CipherAlgorithm):

    def encrypt(self, text, key):
        key = key.encode()          # 16 byte
        cipher = AES.new(key, AES.MODE_ECB)
        encrypted = cipher.encrypt(pad(text.encode(), AES.block_size))
        return base64.b64encode(encrypted).decode()

    def decrypt(self, text, key):
        key = key.encode()
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted = unpad(
            cipher.decrypt(base64.b64decode(text)),
            AES.block_size
        )
        return decrypted.decode()
