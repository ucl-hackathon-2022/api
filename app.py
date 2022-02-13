from datetime import datetime
from pickle import GET
from flask import Flask, redirect, request
from src.email import emailService, emailMessageFormat
from match_location_id import locations_id_map
import requests

app = Flask(__name__)

# Global variables
API_TOKEN = 'uclapi-c534250c5533a5e-969273a8d8b716f-172fc10b1563d07-72b9a381d300f82'
CLIENT_ID = '7083760871512299.0586240432827629'
CLIENT_SECRET = '5110d3ae18ef449a6a4f2a9a489f071ac5c03e8eb3acb05d9a7081067589f36d'
RECEIVER_EMAIL = 'example.api.ucl.sender@gmail.com'
PASSWORD = 'Example1234'

app.config['DEBUG'] = True

# # Temp
# locations_id_map = {'id_1': {'facility_type': 'bathroom',
#                              'location': 'Wilkins'},
#                     'id_2': {'facility_type': 'classroom',
#                              'location': 'Main Quad Pop-up Hub Room 101'}}


@app.route('/', methods=['GET'])
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


url = f"https://uclapi.com/oauth/authorise/?client_id={CLIENT_ID}&state=1"

# Posting data to the client
@app.route('/login')
def uclapi_login():
    return redirect(url)

# # Posting data to the client
# @app.route('/complete')
# def uclapi_complete():
#     return redirect(url)

@app.route('/callback')
def receive_callback():
    # receive parameters 
    # result = request.args.get('result')
    code = request.json['code']
    # state = request.args.get('state')
    params = {
        "client_secret": CLIENT_SECRET,
        "client_id ": CLIENT_ID,
        "code": code,
    }
    r = requests.get('https://uclapi.com/oauth/token', params=params)
    print(r.json())
    # e.g. request an auth token from /oauth/token
    return 'done'

# @app.route('/oauth', methods=['GET'])
# def receive_callback():
#     # receive parameters
#     result = request.json['result']
#     code = request.json['code']
#     state = request.json['state']

#     print(request)
#     print(result)
#     print('code', code)
#     if result == 1:
#         return state, 200
#     print(request)
#     # do something with these parameters
#     # e.g. request an auth token from /oauth/token
#     '''
#     params = {
#         "client_id": "123.456",
#         "code": "1",
#         "client_secret": "secret",
#     }
#     r = request.get("https://uclapi.com/oauth/token", params=params)
#     print(r.json())
#     '''
#     return code, 200

@app.route('/report', methods=['POST'])
def report():
    id = request.json['id']
    event = request.json['event']
    print(id)
    # id = "id_1"
    locations_map = locations_id_map[id]
    # Parameters to pass
    date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    facility_type = locations_map['facility_type']
    location = locations_map['location']
    # event = "tissue"
    userEmail = "a@example.com"

    email = emailService(RECEIVER_EMAIL, RECEIVER_EMAIL, PASSWORD)
    message = emailMessageFormat(userEmail, date, location, event, facility_type)
    print(message.getMessage())
    email.send("Report Issue", message.getMessage())

    return 'done', 200

# @app.route('/sendEmail', methods=['GET'])
# def email():
#     email = emailService(RECEIVER_EMAIL, RECEIVER_EMAIL, PASSWORD)
#     message = emailMessageFormat("john@gmail.com", datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), "Location", "event", "bathroom")
#     print(message.getMessage())
#     email.send("Report Issue", message.getMessage())
#     return "done", 200

if __name__ == '__main__':
    app.run()
