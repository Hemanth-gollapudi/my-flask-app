from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/message')
def get_message():
    return jsonify({'message': 'Hello from hemanth!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)   # Changed to 9000