import datetime

from flask import Flask, redirect, request
import hashlib

app = Flask(__name__)

# Global variables
API_TOKEN = 'uclapi-c534250c5533a5e-969273a8d8b716f-172fc10b1563d07-72b9a381d300f82'
CLIENT_ID = '7083760871512299.0586240432827629'
CLIENT_SECRET = '5110d3ae18ef449a6a4f2a9a489f071ac5c03e8eb3acb05d9a7081067589f36d'
RECEIVER_EMAIL = 'example.api.ucl.sender@gmail.com'

app.config['DEBUG'] = True


@app.route('/', methods=['POST'])
def hello():
    return 'hello world', 200

# Posting data to the client
@app.route('/callbackParam', methods=['POST'])
def addData():
    '''Data that we need from the user.'''
    username = request.json['username']
    password = request.json['password']
    print(request)
    res = {
        'username': username,
        'password': password
    }
    return res, 200


@app.route('/rToilet', methods=['POST'])
def addData():
    time = datetime.datetime.now()  # time the user submitted the report
    event = request.json['username']  # eg miss toilet paper, broken PC
    location_id = 1  # location id of the QR code; real location in a database
    res = {
        'time': time,
        'event': event,
        'email': 'abc@example.com',
        'location_id': location_id
    }
    email = email()
    return res, 200


if __name__ == '__main__':
    app.run()
