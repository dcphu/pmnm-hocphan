# b12_counter.py
from flask import Flask, request, jsonify

app = Flask(__name__)
app.json.ensure_ascii = False

counter = 0

@app.route("/counter", methods=["GET", "POST", "DELETE"])
def handle_counter():
    global counter

    if request.method == "GET":
        return jsonify({"counter": counter})

    elif request.method == "POST":
        try:
            step = int(request.args.get("step", 1))
        except ValueError:
            step = 1

        counter += step
        return jsonify({
            "counter": counter,
            "message": f"Đã tăng {step}"
        })

    elif request.method == "DELETE":
        counter = 0
        return "", 204

if __name__ == "__main__":
    app.run(debug=True, port=8000)

