import base64
from kripto.cipher_base import CipherAlgorithm

class XorCipher(CipherAlgorithm):

    def encrypt(self, text, key):
        result = bytes(
            [ord(text[i]) ^ ord(key[i % len(key)]) for i in range(len(text))]
        )
        return base64.b64encode(result).decode()

    def decrypt(self, text, key):
        data = base64.b64decode(text)
        result = bytes(
            [data[i] ^ ord(key[i % len(key)]) for i in range(len(data))]
        )
        return result.decode()
