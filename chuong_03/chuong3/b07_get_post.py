# b07_get_post.py
from flask import Flask, url_for

app = Flask(__name__)

@app.get("/login")
def login_form():
    action_url = url_for("login_action")
    return f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head><meta charset="UTF-8"><title>Đăng nhập</title></head>
    <body style="font-family: Arial; padding: 20px;">
        <h2>Đăng nhập</h2>
        <form action="{action_url}" method="post">
            <input type="text" name="username" placeholder="Tên đăng nhập">
            <button type="submit">Đăng nhập</button>
        </form>
    </body>
    </html>
    """

@app.post("/login")
def login_action():
    return "Đã nhận yêu cầu đăng nhập (POST)."

if __name__ == "__main__":
    app.run(debug=True, port=8000)

