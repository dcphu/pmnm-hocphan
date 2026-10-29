# b06_url_for.py
from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "Trang chủ"

@app.route("/about")
def about():
    return "Giới thiệu"

@app.route("/post/<int:post_id>")
def post_detail(post_id):
    return f"Chi tiết bài viết: {post_id}"

@app.route("/user/<username>")
def user_profile(username):
    return f"Trang cá nhân: {username}"

@app.route("/search")
def search():
    return "Tìm kiếm"

@app.route("/menu")
def menu():
    link_a = url_for("about")
    link_b = url_for("post_detail", post_id=7)
    link_c = url_for("post_detail", post_id=7, lang="vi")
    link_d = url_for("user_profile", username="Nguyễn An")
    link_e = url_for("search", q="flask & python")

    return f"""
    <h2>Menu điều hướng (url_for)</h2>
    <ul>
        <li><a href="{link_a}">a. {link_a}</a></li>
        <li><a href="{link_b}">b. {link_b}</a></li>
        <li><a href="{link_c}">c. {link_c}</a></li>
        <li><a href="{link_d}">d. {link_d}</a></li>
        <li><a href="{link_e}">e. {link_e}</a></li>
    </ul>
    """

if __name__ == "__main__":
    app.run(debug=True, port=8000)

