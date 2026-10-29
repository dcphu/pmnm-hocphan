# b09_calc.py
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": error.description}), 400

def format_num_expr(n):
    return str(int(n)) if n == int(n) else str(n)

@app.route("/calc")
def calculate():
    a_raw = request.args.get("a")
    b_raw = request.args.get("b")
    if a_raw is None or b_raw is None:
        abort(400, description="Thiếu tham số 'a' hoặc 'b'.")

    try:
        a = float(a_raw)
        b = float(b_raw)
    except ValueError:
        abort(400, description="Giá trị của 'a' hoặc 'b' không phải là số hợp lệ.")

    op = request.args.get("op", "add")
    valid_ops = {"add": "+", "sub": "-", "mul": "*", "div": "/"}
    if op not in valid_ops:
        abort(400, description=f"Phép toán '{op}' không hợp lệ. Chỉ chấp nhận: add, sub, mul, div.")

    if op == "div" and b == 0:
        abort(400, description="Lỗi chia cho 0.")

    calc_map = {
        "add": a + b,
        "sub": a - b,
        "mul": a * b,
        "div": a / b
    }
    result = calc_map[op]
    expression = f"{format_num_expr(a)} {valid_ops[op]} {format_num_expr(b)}"

    return jsonify({
        "a": a,
        "b": b,
        "op": op,
        "expression": expression,
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True, port=8000)

