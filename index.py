from flask import Flask

app = Flask(__name__)

@app.route("/ali")
def hi_ali():
    return "Hi Ali Bhai"

@app.route("/armaghan")
def hi_armaghan():
    return "Hi Armaghan Bhai"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
