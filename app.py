from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Monitor AFPESP funcionando! Agora vamos completar o código todo."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
