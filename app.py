from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask API is running! Use /api/greet or /api/sum"

@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify({'message': 'Hello from the Cloud Web Service!'})

@app.route('/api/sum', methods=['POST'])
def sum_values():
    data = request.get_json()
    result = data['a'] + data['b']
    return jsonify({'sum': result})

if __name__ == '__main__':
    app.run(debug=True)
