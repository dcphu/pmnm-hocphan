# b08_request_info.py
from flask import Flask, request
from markupsafe import escape
import json

app = Flask(__name__)

@app.route("/info", methods=["GET", "POST"])
def request_info():
    method = escape(request.method)
    path = escape(request.path)
    full_path = escape(request.full_path)
    url = escape(request.url)
    remote_addr = escape(request.remote_addr or "Unknown")
    user_agent = escape(request.headers.get("User-Agent", "N/A"))

    query_args = {k: request.args.getlist(k) if len(request.args.getlist(k)) > 1 else request.args.get(k) for k in request.args}
    query_args_escaped = escape(json.dumps(query_args, ensure_ascii=False))

    return f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head><meta charset="UTF-8"><title>Thông tin Request</title></head>
    <body style="font-family: Arial; padding: 20px;">
        <h2>Bảng Thông Tin Request</h2>
        <table border="1" cellpadding="8" style="border-collapse: collapse;">
            <tr><th>Thuộc tính</th><th>Giá trị</th></tr>
            <tr><td>Phương thức</td><td>{method}</td></tr>
            <tr><td>Đường dẫn</td><td>{path}</td></tr>
            <tr><td>Đường dẫn kèm query</td><td>{full_path}</td></tr>
            <tr><td>URL đầy đủ</td><td>{url}</td></tr>
            <tr><td>Địa chỉ IP</td><td>{remote_addr}</td></tr>
            <tr><td>User-Agent</td><td>{user_agent}</td></tr>
            <tr><td>Các tham số query</td><td>{query_args_escaped}</td></tr>
        </table>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, port=8000)

