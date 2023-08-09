from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    try:
        # Assuming the request data is sent as JSON containing 'num1' and 'num2'
        data = request.json
        num1 = data.get('first')
        num2 = data.get('second')

        if num1 is None or num2 is None:
            return "Invalid input: 'num1' and 'num2' must be provided as JSON data.", 400

        result = num1 + num2

        return {
            'result': result
        }, 200

    except Exception as e:
        return str(e), 500
    

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    try:
        # Assuming the request data is sent as JSON containing 'num1' and 'num2'
        data = request.json
        num1 = data.get('first')
        num2 = data.get('second')

        if num1 is None or num2 is None:
            return jsonify({"error": "Invalid input: 'num1' and 'num2' must be provided as JSON data."}), 400

        result = num1 - num2

        return jsonify({"result": result}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')