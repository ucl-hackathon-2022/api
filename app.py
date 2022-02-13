from datetime import datetime
from pickle import GET
from flask import Flask, redirect, request
from flask_cors import CORS
from src.email import emailService, emailMessageFormat
from match_location_id import locations_id_map
import requests
import gunicorn


app = Flask(__name__)
cors = CORS(app)


# Global variables
RECEIVER_EMAIL = 'example.api.ucl.sender@gmail.com'
PASSWORD = 'Example1234'

app.config['DEBUG'] = True

# for testing in the remote sever
@app.route('/', methods=['GET'])
def hello():
    return 'hello world', 200

# for integrating with the frontend solution
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

if __name__ == '__main__':
    app.run()
