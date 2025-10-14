from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Caesar Cipher şifreleme fonksiyonu
def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    method = data.get("method")
    key = int(data.get("key"))
    message = data.get("message")

    if method == "caesar":
        encrypted = caesar_cipher_encrypt(message, key)
        return jsonify({"encrypted": encrypted})
    else:
        return jsonify({"error": "Desteklenmeyen şifreleme yöntemi"}), 400

if __name__ == '__main__':
    app.run(debug=True)
