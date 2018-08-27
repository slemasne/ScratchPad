# Python code to illustrate Sending mail from
# Import the packages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import os

# Define username and password for SendGrid API
user_name = "apikey"
pw = os.environ["API_KEY"]
#email_address = os.environ["email_address"]
email_address = "stephenlemasney@gmail.com"
filename = "transactions.csv"
file_path = "/Users/slemasne/PycharmProjects/ScratchPad/files/transactions.csv"

# creates SMTP session
# start TLS for security
# Authentication
server = smtplib.SMTP('smtp.sendgrid.net', 587)
server.starttls()
server.login(user_name, pw)

# Create html string from html file
now = datetime.now().strftime("%c")
with open("email_message.html", "r") as f:
    html_string = f.read().format(now)

# Create message to be used in Email
msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = email_address
msg['Subject'] = "Python Email Update"
msg.attach(MIMEText(html_string, 'html'))

# Create attachment
attachment = open(file_path, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)

# Login and send email
server.login(user_name, pw)
text = msg.as_string()
server.sendmail(email_address, email_address, text)
server.quit()