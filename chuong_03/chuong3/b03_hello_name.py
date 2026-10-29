# b03_hello_name.py
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/hello/", defaults={"name": "bạn"})
@app.route("/hello/<name>")
def greet(name):
    return f"<h1>Xin chào, {escape(name)}!</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=8000)

