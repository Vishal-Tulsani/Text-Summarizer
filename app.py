from flask import Flask, jsonify, request
from Nltk_Summarizer import summary
import json

# app
app = Flask(__name__)

# routes
@app.route('/',methods = ['POST'])

def summarizer():
    file_data = request.args.get('data')
    
    return jsonify(summary(file_data))


if __name__ == '__main__':
    app.run(port = 5000, debug=True)
