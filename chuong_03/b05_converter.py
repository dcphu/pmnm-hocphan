# b05_converter.py
from flask import Flask, jsonify, url_for
from werkzeug.routing import BaseConverter, ValidationError

app = Flask(__name__)

class ListConverter(BaseConverter):
    regex = r"-?\d+(?:,-?\d+)*"

    def to_python(self, value):
        try:
            return [int(item) for item in value.split(",")]
        except ValueError:
            raise ValidationError()

    def to_url(self, value):
        if isinstance(value, list):
            return ",".join(str(x) for x in value)
        return str(value)

app.url_map.converters["list"] = ListConverter

@app.route("/sum/<list:numbers>")
def sum_numbers(numbers):
    return jsonify({
        "numbers": numbers,
        "sum": sum(numbers)
    })

if __name__ == "__main__":
    app.run(debug=True, port=8000)

