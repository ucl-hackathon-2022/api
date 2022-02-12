from flask import Flask, redirect, request
import hashlib

app = Flask(__name__)

API_TOKEN = 'uclapi-c534250c5533a5e-969273a8d8b716f-172fc10b1563d07-72b9a381d300f82'
CLIENT_ID = '7083760871512299.0586240432827629'
CLIENT_SECRET = '5110d3ae18ef449a6a4f2a9a489f071ac5c03e8eb3acb05d9a7081067589f36d'

app.config['DEBUG'] = True

@app.route('/', methods=['POST'])
def hello():
    return 'hello world', 200

#for posting data to the client
@app.route('/callbackParam', methods=['POST'])
def addData():
    username = request.json['username']
    password = request.json['password']
    res = {
        'username': username,
        'password': password
    }
    return res, 200

if __name__ == '__main__':
    app.run()