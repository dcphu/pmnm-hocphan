# b10_api_tien_ich.py
from flask import Flask, jsonify, request, abort
from datetime import datetime
import random

app = Flask(__name__)
app.json.ensure_ascii = False

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": error.description}), 400

@app.route("/api/time")
def get_time():
    now = datetime.now()
    thu_map = {
        0: "Thứ Hai", 1: "Thứ Ba", 2: "Thứ Tư",
        3: "Thứ Năm", 4: "Thứ Sáu", 5: "Thứ Bảy", 6: "Chủ Nhật"
    }
    return jsonify({
        "iso": now.isoformat(),
        "date": now.strftime("%d/%m/%Y"),
        "time": now.strftime("%H:%M:%S"),
        "weekday": thu_map[now.weekday()]
    })

@app.route("/api/random")
def get_random():
    try:
        min_val = int(request.args.get("min", 1))
        max_val = int(request.args.get("max", 100))
        count = int(request.args.get("count", 1))
    except ValueError:
        abort(400, description="Các tham số 'min', 'max', 'count' phải là số nguyên.")

    if min_val > max_val:
        abort(400, description="Tham số 'min' không được lớn hơn 'max'.")

    if count < 1 or count > 100:
        abort(400, description="Tham số 'count' phải nằm trong khoảng từ 1 đến 100.")

    return jsonify({
        "min": min_val,
        "max": max_val,
        "count": count,
        "numbers": [random.randint(min_val, max_val) for _ in range(count)]
    })

if __name__ == "__main__":
    app.run(debug=True, port=8000)

