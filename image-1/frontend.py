import os
from flask import Flask
import datetime
import requests
import pytz
from datetime import date

app = Flask(__name__)

@app.route('/')
def hello():  
   
    
    response = requests.get('http://internproject-backend:5100/response')
    
    pakistan_timezone = pytz.timezone("Asia/Karachi")
    e = datetime.datetime.now(pakistan_timezone)   
    data = response.json()
    return f"{e.day}/{e.month}/{e.year} {e.hour}:{e.minute} Hello {data['name']}!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5200)

