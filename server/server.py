import socket
from kripto.util.cipher_factory import get_cipher

HOST = "127.0.0.1"
PORT = 5555

cipher = get_cipher("AES")
key = "1234567890123456"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Sunucu bekliyor...")

    conn, addr = s.accept()
    with conn:
        print("Bağlandı:", addr)
        data = conn.recv(4096).decode()
        print("Gelen Şifreli:", data)

        decrypted = cipher.decrypt(data, key)
        print("Çözülen Mesaj:", decrypted)
