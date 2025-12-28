import numpy as np
from kripto.cipher_base import CipherAlgorithm

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class HillCipher(CipherAlgorithm):

    def encrypt(self, text, key):
        key_matrix = np.array(key)
        text = text.upper().replace(" ", "")

        if len(text) % 2 != 0:
            text += 'X'

        result = ""
        for i in range(0, len(text), 2):
            pair = [ALPHABET.index(text[i]), ALPHABET.index(text[i+1])]
            encrypted = key_matrix.dot(pair) % 26
            result += ALPHABET[encrypted[0]] + ALPHABET[encrypted[1]]

        return result

    def decrypt(self, text, key):
        key_matrix = np.array(key)
        det = int(round(np.linalg.det(key_matrix)))
        det_inv = pow(det, -1, 26)
        adj = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
        inv_key = (det_inv * adj) % 26

        result = ""
        for i in range(0, len(text), 2):
            pair = [ALPHABET.index(text[i]), ALPHABET.index(text[i+1])]
            decrypted = inv_key.dot(pair) % 26
            result += ALPHABET[decrypted[0]] + ALPHABET[decrypted[1]]

        return result
