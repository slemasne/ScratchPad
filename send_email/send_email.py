# Python code to illustrate Sending mail from
# Import the packages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import os

# Define username and password for SendGrid API
user_name = "apikey"
pw = os.environ["API_KEY"]
email_address = "stephenlemasney@gmail.com"

# creates SMTP session
# start TLS for security
# Authentication
server = smtplib.SMTP('smtp.sendgrid.net', 587)
server.starttls()
server.login(user_name, pw)

# Create html string from html file

now = datetime.now().strftime("%c")
with open("send_email/email_message.html", "r") as f:
    html_string = f.read().format(now)

# Create message to be used in Email
msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = email_address
msg['Subject'] = "Python Email Update"
msg.attach(MIMEText(html_string, 'html'))

# Login and send email
server.login(user_name, pw)
text = msg.as_string()
server.sendmail(email_address, email_address, text)
server.quit()