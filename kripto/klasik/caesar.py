from kripto.cipher_base import CipherAlgorithm

class CaesarCipher(CipherAlgorithm):

    def encrypt(self, text, key):
        shift = int(key)
        result = ""

        for c in text:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                result += chr((ord(c) - base + shift) % 26 + base)
            else:
                result += c
        return result

    def decrypt(self, text, key):
        return self.encrypt(text, 26 - int(key))
