import smtpilib #This is showing a not found error (TODO)
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
            server.login(sender_email, password)
            print("Connection established successfully.")
            return server, sender_email, receiver_email
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None
    
if __name__ == "__main__":
    server, sender_email, receiver_email = sendEmail()
    if server:
        print(f"Ready to send email from {sender_email} to {receiver_email}")