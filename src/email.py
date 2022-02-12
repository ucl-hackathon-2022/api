from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class emailMessageFormat():
    def __init__(self, email, time, location, event, facility_type):
        self.email = email 
        self.time = time
        self.location = location
        self.event = event
        #[bathroom/corridor/common space/classroom/laboratory/library]
        self.facility_type = facility_type
    
    def getMessage(self):
        head = "Dear Estates, \n\n" 
        message = "The UCL member with the email {} reported a problem at {}. The {} located in {} has the following issue: {}.".format(self.email, self.time, self.facility_type, self.location, self.event)
        ending = "\n\nWe appreciate a quick resolution of the problem."
        body = head + message + ending
        print(body)
        return body

class emailService():
    
    def __init__(self, senderEmail, recieverEmail, password):
        self.msg = MIMEMultipart()
        self.msg['From'] = senderEmail
        self.msg['To'] = recieverEmail
        self.password = password

    def send(self, header, message):
        self.msg['Subject'] = header
        self.msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(self.msg['From'], self.password)
        server.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string())
        server.quit()