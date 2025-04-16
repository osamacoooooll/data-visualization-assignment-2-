from flask import Flask, request, jsonify
import json
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

packages = []

@app.route('/receive', methods=['GET'])
def receive_package():
    data = request.args.get('data')
    if data:
        try:
            package = json.loads(data)
            packages.append(package)
            return jsonify({'status': 'success'})
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    return jsonify({'error': 'no data provided'}), 400

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(packages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
