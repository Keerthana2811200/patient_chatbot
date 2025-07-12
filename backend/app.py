# app.py
from flask import Flask, render_template, request, jsonify
from chatbot import get_bot_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def respond():
    user_input = request.json['message']
    response = get_bot_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
