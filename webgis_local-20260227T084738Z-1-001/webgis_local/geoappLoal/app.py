from flask import Flask, jsonify, render_template
from flask_cors import CORS
import json, os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    geojson_path = os.path.join('data', 'data.geojson')
    with open(geojson_path) as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
