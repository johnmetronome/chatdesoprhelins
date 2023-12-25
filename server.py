from flask import Flask, render_template, request, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

messages = []

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/send', methods=['POST'])
def send():
    username = request.json.get('username')
    message = request.json.get('message')
    timestamp = datetime.now().strftime("%H:%M:%S")  # Formatage de l'heure actuelle
    messages.append({'username': username, 'message': message, 'timestamp': timestamp})
    return jsonify({'status': 'success'})

@app.route('/receive')
def receive():
    return jsonify(messages)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
