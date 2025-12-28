from kripto.cipher_base import CipherAlgorithm

class VigenereCipher(CipherAlgorithm):

    def encrypt(self, text, key):
        result = ""
        key = key.upper()
        j = 0

        for c in text:
            if c.isalpha():
                shift = ord(key[j % len(key)]) - ord('A')
                base = ord('A') if c.isupper() else ord('a')
                result += chr((ord(c) - base + shift) % 26 + base)
                j += 1
            else:
                result += c
        return result

    def decrypt(self, text, key):
        result = ""
        key = key.upper()
        j = 0

        for c in text:
            if c.isalpha():
                shift = ord(key[j % len(key)]) - ord('A')
                base = ord('A') if c.isupper() else ord('a')
                result += chr((ord(c) - base - shift + 26) % 26 + base)
                j += 1
            else:
                result += c
        return result
