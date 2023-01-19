import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/response')
def hello():
    name = os.environ.get("NAME")
    message = f"{name}!"
    return jsonify(name=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)


