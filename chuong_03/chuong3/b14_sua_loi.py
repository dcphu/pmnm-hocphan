# b14_sua_loi.py
from flask import Flask, request, url_for

app = Flask(__name__)

# Sửa lỗi 2: url_for("home") -> url_for("index")
@app.route("/")
def index():
    return f'<a href="{url_for("index")}">Trang chủ</a> | <a href="{url_for("contact")}">Liên hệ</a>'

# Sửa lỗi 1: def index() trùng lặp -> def about()
@app.route("/about")
def about():
    return "Giới thiệu"

# Sửa lỗi 3: <int:id> -> <int:post_id>
@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Bài viết số {post_id}"

# Sửa lỗi 4: Thêm return khi score < 5
@app.route("/grade/<int:score>")
def grade(score):
    if score >= 8:
        return "Giỏi"
    if score >= 5:
        return "Đạt"
    return "Chưa đạt"

# Sửa lỗi 5: Thêm methods=["GET", "POST"]
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return "Đã gửi liên hệ"
    return '<form method="post"><button type="submit">Gửi liên hệ</button></form>'

if __name__ == "__main__":
    app.run(debug=True, port=8000)

