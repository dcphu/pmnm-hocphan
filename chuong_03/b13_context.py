# b13_context.py
from flask import Flask, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "Trang chủ"

@app.route("/about")
def about():
    return "Giới thiệu"

@app.route("/search")
def search():
    return "Tìm kiếm"

if __name__ == "__main__":
    app.run(debug=True, port=8000)

