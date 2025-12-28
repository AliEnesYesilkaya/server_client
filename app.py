from flask import Flask, render_template, request, jsonify
from kripto.util.cipher_factory import get_cipher

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# İSTEMCİ – ŞİFRELEME
@app.route("/encrypt", methods=["POST"])
def encrypt():
    algo = request.form["algorithm"]
    key = request.form["key"]
    message = request.form["message"]

    cipher = get_cipher(algo)

    # Hill özel durum
    if algo == "HILL":
        key = eval(key)  # [[3,3],[2,5]]

    encrypted = cipher.encrypt(message, key)
    return jsonify({"result": encrypted})


# SUNUCU – DEŞİFRELEME
@app.route("/decrypt", methods=["POST"])
def decrypt():
    algo = request.form["algorithm"]
    key = request.form["key"]
    message = request.form["message"]

    cipher = get_cipher(algo)

    if algo == "HILL":
        key = eval(key)

    decrypted = cipher.decrypt(message, key)
    return jsonify({"result": decrypted})


if __name__ == "__main__":
    app.run(debug=True)
