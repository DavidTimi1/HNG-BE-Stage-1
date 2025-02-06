from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Helper functions
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)


def get_properties(n):
    properties = []

    # exclude negative numbers
    if n >= 0 and sum(int(digit) ** len(str(n)) for digit in str(n)) == n:
        properties.append("armstrong")

    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    return properties


@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    try:
        number = int(number)

    except ValueError:
        return jsonify({
            "number": request.args.get('number'),
            "error": True
        }), 400
    

    # Fetch a fun fact from Numbers API
    response = requests.get(f"http://numbersapi.com/{number}/math?json")
    if response.status_code == 200:
        fun_fact = response.json().get("text", "No fun fact available.")
    else:
        fun_fact = "No fun fact available."

    # Generate the response
    result = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": get_properties(number),
        "digit_sum": sum(int(digit) if digit != "-" else 0 for digit in str(number)),
        "fun_fact": fun_fact
    }

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
