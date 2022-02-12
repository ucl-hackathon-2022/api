from datetime import datetime
from pickle import GET

from flask import Flask, redirect, request
import hashlib

from src.email import emailService, emailMessageFormat

app = Flask(__name__)

# Global variables
API_TOKEN = 'uclapi-c534250c5533a5e-969273a8d8b716f-172fc10b1563d07-72b9a381d300f82'
CLIENT_ID = '7083760871512299.0586240432827629'
CLIENT_SECRET = '5110d3ae18ef449a6a4f2a9a489f071ac5c03e8eb3acb05d9a7081067589f36d'
RECEIVER_EMAIL = 'example.api.ucl.sender@gmail.com'
PASSWORD = 'Example1234'

app.config['DEBUG'] = True

# Temp
locations_id_map = {'id_1': {'facility_type': 'bathroom',
                             'location': 'Wilkins'},
                    'id_2': {'facility_type': 'classroom',
                             'location': 'Main Quad Pop-up Hub Room 101'}}


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

@app.route('/report', methods=['POST'])
def report():
    id = request.json['id']
    print(id)
    # id = "id_1"
    locations_map = locations_id_map[id]
    #params
    date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    facility_type = locations_map['facility_type']
    location = locations_map['location']
    event = "tissue"
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

# @app.route('/rToilet', methods=['POST'])
# def t():
#     time = datetime.datetime.now()  # time the user submitted the report
#     event = request.json['username']  # eg miss toilet paper, broken PC
#     location_id = 1
#     res = {
#         'time': time,
#         'event': event,
#         'email': 'abc@example.com',
#         'location_id': location_id
#     }
#     return res, 200


if __name__ == '__main__':
    app.run()
