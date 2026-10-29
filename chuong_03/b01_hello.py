# b01_hello.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Xin chào, Flask!</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=8000)

