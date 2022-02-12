from flask import Flask, request
import hashlib

app = Flask(__name__)

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