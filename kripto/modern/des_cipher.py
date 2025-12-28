import base64
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from kripto.cipher_base import CipherAlgorithm


class DESCipher(CipherAlgorithm):

    def encrypt(self, text, key):
        key = key.encode()          # 8 byte olmalı
        cipher = DES.new(key, DES.MODE_ECB)
        encrypted = cipher.encrypt(pad(text.encode(), DES.block_size))
        return base64.b64encode(encrypted).decode()

    def decrypt(self, text, key):
        key = key.encode()
        cipher = DES.new(key, DES.MODE_ECB)
        decrypted = unpad(
            cipher.decrypt(base64.b64decode(text)),
            DES.block_size
        )
        return decrypted.decode()
