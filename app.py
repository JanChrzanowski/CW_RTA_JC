from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def puropose():
    return "This site uses perceprton model"

if __name__ == '__main__':
    app.run(debug=True)