function showClient() {
    document.getElementById("client").style.display = "block";
    document.getElementById("server").style.display = "none";
}

function showServer() {
    document.getElementById("client").style.display = "none";
    document.getElementById("server").style.display = "block";
}

function encrypt() {
    fetch("/encrypt", {
        method: "POST",
        body: new URLSearchParams({
            algorithm: enc_algo.value,
            key: enc_key.value,
            message: enc_msg.value
        })
    })
    .then(res => res.json())
    .then(data => enc_result.innerText = data.result);
}

function decrypt() {
    fetch("/decrypt", {
        method: "POST",
        body: new URLSearchParams({
            algorithm: dec_algo.value,
            key: dec_key.value,
            message: dec_msg.value
        })
    })
    .then(res => res.json())
    .then(data => dec_result.innerText = data.result);
}
