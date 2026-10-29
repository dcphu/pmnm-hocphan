# b04_square.py
from flask import Flask, abort

app = Flask(__name__)

@app.route("/square/<n>")
def square(n):
    try:
        val = int(n)
        return f"Bình phương của {val} là: {val ** 2}"
    except ValueError:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True, port=8000)

