from flask import Flask, jsonify
import random

app = Flask(__name__)
data = [random.randint(1, 100) for _ in range(10000)]

@app.route('/data')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run()
