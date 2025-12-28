import socket
from kripto.util.cipher_factory import get_cipher

HOST = "127.0.0.1"
PORT = 5555

cipher = get_cipher("AES")
key = "1234567890123456"   # AES için 16 byte
message = "Merhaba Kriptoloji"

encrypted = cipher.encrypt(message, key)
print("Şifreli Mesaj:", encrypted)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(encrypted.encode())
