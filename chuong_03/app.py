from flask import Flask, render_template, jsonify, abort, request, url_for

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Dữ liệu sách (≥ 4 cuốn)
# ---------------------------------------------------------------------------
BOOKS = [
    {
        "id": 1,
        "title": "Lập trình Python cơ bản",
        "author": "Nguyễn Văn A",
        "year": 2020,
        "category": "Lập trình",
        "available": True,
    },
    {
        "id": 2,
        "title": "Cấu trúc dữ liệu và giải thuật",
        "author": "Trần Thị B",
        "year": 2019,
        "category": "Khoa học máy tính",
        "available": False,
    },
    {
        "id": 3,
        "title": "Flask Web Development",
        "author": "Miguel Grinberg",
        "year": 2018,
        "category": "Lập trình",
        "available": True,
    },
    {
        "id": 4,
        "title": "Trí tuệ nhân tạo - Tiếp cận hiện đại",
        "author": "Stuart Russell",
        "year": 2021,
        "category": "Trí tuệ nhân tạo",
        "available": True,
    },
    {
        "id": 5,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "year": 2008,
        "category": "Lập trình",
        "available": False,
    },
    {
        "id": 6,
        "title": "Mạng máy tính",
        "author": "Andrew S. Tanenbaum",
        "year": 2017,
        "category": "Mạng máy tính",
        "available": True,
    },
]


def _get_book(book_id):
    """Trả về sách theo id, hoặc None nếu không tìm thấy."""
    return next((b for b in BOOKS if b["id"] == book_id), None)


def _all_categories():
    """Trả về danh sách thể loại duy nhất, có thứ tự."""
    seen = []
    for b in BOOKS:
        if b["category"] not in seen:
            seen.append(b["category"])
    return seen


# ---------------------------------------------------------------------------
# Routes HTML
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    total = len(BOOKS)
    available = sum(1 for b in BOOKS if b["available"])
    return render_template("index.html", total=total, available=available)


@app.route("/books")
def books():
    category = request.args.get("category", "").strip()
    if category:
        filtered = [b for b in BOOKS if b["category"] == category]
    else:
        filtered = BOOKS
    categories = _all_categories()
    return render_template(
        "books.html",
        books=filtered,
        categories=categories,
        selected_category=category,
    )


@app.route("/books/<int:book_id>")
def book_detail(book_id):
    book = _get_book(book_id)
    if book is None:
        abort(404)
    return render_template("book_detail.html", book=book)


# ---------------------------------------------------------------------------
# Routes JSON API
# ---------------------------------------------------------------------------

@app.route("/api/books")
def api_books():
    return jsonify(BOOKS)


@app.route("/api/books/<int:book_id>")
def api_book_detail(book_id):
    book = _get_book(book_id)
    if book is None:
        return jsonify({"error": f"Không có sách với ID = {book_id}"}), 404
    return jsonify(book)


# ---------------------------------------------------------------------------
# Trang 404 tuỳ biến
# ---------------------------------------------------------------------------

@app.errorhandler(404)
def page_not_found(e):
    # Phân biệt request API vs. trang HTML
    if request.path.startswith("/api/"):
        # Với API, trả JSON (nếu errorhandler được gọi từ abort trong API)
        # Trường hợp này thực ra không xảy ra vì API tự trả JSON; giữ để an toàn.
        return jsonify({"error": "Không tìm thấy tài nguyên"}), 404
    # Lấy book_id từ path nếu có dạng /books/<id>
    message = None
    parts = request.path.strip("/").split("/")
    if len(parts) == 2 and parts[0] == "books":
        try:
            bid = int(parts[1])
            message = f"Không có sách với ID = {bid}"
        except ValueError:
            pass
    if message is None:
        message = f"Trang '{request.path}' không tồn tại."
    return render_template("404.html", message=message), 404


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)