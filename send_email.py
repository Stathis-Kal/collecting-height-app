from email.mime.text import MIMEText
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(email, height, avg_height, count):
    sender = os.environ.get("user")
    sender_pwd = os.environ.get("password")
    receiver = email
    subject = "Height Data 📊"
    message = "Hello there 👋, your height is <strong>%s</strong> cm 😄. The average height of all records is <strong>%f</strong> 😲 and that is calculated out of <strong>%g</strong> people! 👏" % (
        height, avg_height, count)

    msg = MIMEText(message, 'html')
    msg["Subject"] = subject
    msg["To"] = receiver
    msg["From"] = sender

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, sender_pwd)
    gmail.send_message(msg)
