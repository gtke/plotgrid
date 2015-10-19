from flask import Flask, jsonify, render_template
import requests
import json
from datetime import datetime
from flaskrun import create_app

app = create_app()
app.config.from_object('config')

TIME_WINDOW = app.config['time_window']
ENDPOINT = app.config['ENDPOINT']

@app.route('/', methods=['GET'])
def get():
    return render_template('index.html', time_window=TIME_WINDOW)

@app.route('/data', methods=['GET'])
def data():
    response = requests.get(ENDPOINT).content
    data = json.loads(response)
    data['timestamp'] = datetime.now().isoformat()
    return json.dumps(data)

@app.route('/ping', methods=['GET'])
def pong():
    return jsonify({
        'status': 'alive'
    })

if __name__ == '__main__':
    app.run(debug=True)
