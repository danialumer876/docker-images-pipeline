import os
from flask import Flask
import datetime
import requests
from datetime import date

app = Flask(__name__)

@app.route('/')
def hello():  
    response = requests.get('http://backend-service:5100/response')
    e = datetime.datetime.now()
    data = response.json()
    return f"{e.day}/{e.month}/{e.year}  Hello {data['name']}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5200)

