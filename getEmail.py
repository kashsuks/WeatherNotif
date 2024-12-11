import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass4 import getpass

def sendEmail():
    senderEmail = input("Enter your host email: ")
    recieverEmail = input("Enter the reciever email: ")
    
    password = getpass(prompt="Enter your email password: ")
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(senderEmail, password)
            print("Connection established successfully.")
            return server, senderEmail, receiverEmail
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None
    
if __name__ == "__main__":
    server, senderEmail, receiverEmail = sendEmail()
    if server:
        print(f"Ready to send email from {senderEmail} to {receiverEmail}")