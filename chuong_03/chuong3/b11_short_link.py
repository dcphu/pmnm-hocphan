# b11_short_link.py
from flask import Flask, redirect, abort, url_for

app = Flask(__name__)

LINKS = {
    "flask": "https://flask.palletsprojects.com/",
    "python": "https://www.python.org/",
    "github": "https://github.com/",
    "osi": "https://opensource.org/"
}

@app.route("/go/<code>")
def redirect_link(code):
    target_url = LINKS.get(code.lower())
    if not target_url:
        abort(404)
    return redirect(target_url, code=302)

@app.route("/links")
def list_links():
    items = []
    for code, target in LINKS.items():
        short_url = url_for("redirect_link", code=code)
        items.append(f"<li><strong>{code}</strong>: <a href='{short_url}'>{short_url}</a> &rarr; <code>{target}</code></li>")

    return f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head><meta charset="UTF-8"><title>Danh sách link rút gọn</title></head>
    <body style="font-family: Arial; padding: 20px;">
        <h2>Danh Sách Link Rút Gọn</h2>
        <ul>{''.join(items)}</ul>
    </body>
    </html>
    """

@app.errorhandler(404)
def not_found(e):
    links_page = url_for("list_links")
    return f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head><meta charset="UTF-8"><title>404 - Không tìm thấy</title></head>
    <body style="font-family: Arial; text-align: center; padding-top: 50px;">
        <h1 style="color: #dc3545;">404 - Mã link không tồn tại!</h1>
        <p><a href="{links_page}">Quay về danh sách link (/links)</a></p>
    </body>
    </html>
    """, 404

if __name__ == "__main__":
    app.run(debug=True, port=8000)

