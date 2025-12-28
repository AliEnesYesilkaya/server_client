from kripto.klasik.caesar import CaesarCipher
from kripto.klasik.vigenere import VigenereCipher
from kripto.klasik.xor import XorCipher
from kripto.klasik.playfair import PlayfairCipher
from kripto.klasik.hill import HillCipher
from kripto.modern.aes_cipher import AESCipher
from kripto.modern.des_cipher import DESCipher


def get_cipher(name):
    name = name.upper()

    return {
        "CAESAR": CaesarCipher(),
        "VIGENERE": VigenereCipher(),
        "XOR": XorCipher(),
        "PLAYFAIR": PlayfairCipher(),
        "HILL": HillCipher(),
        "AES": AESCipher(),
        "DES": DESCipher()
    }.get(name)
