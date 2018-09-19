#!/usr/bin/python3

import smtplib

sender = ''
receivers = ['']

message = '''This is a test message'''

try:
    smtp_server = smtplib.SMTP(host='', port=25)

except smtplib.socket.gaierror:
    print("Failed to connect to host")

else:
    try:
        #smtp_server.starttls()
        #smtp_server.login('', '')
        print('hello')
    except smtplib.SMTPAuthenticationError:
        print("Failed to Authenticate")
    else:
        try:
            print(message)
            smtp_server.sendmail(sender, receivers, message)
            print("Successfully sent email")
        except Exception:
            print("Error")

#except smtplib.SMTPException:
#    print("Error: unable to send email")


'''
import smtplib

from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

smtp_server = smtplib.SMTP(host='smtp.corelogic.com', port=25)
smtp_server.starttls()
smtp_server.login('', '')

msg = MIMEMultipart()

msg['FROM'] = ''
msg['To'] = ''
msg['subject'] = ''

smtp_server.send_message(msg)
'''
