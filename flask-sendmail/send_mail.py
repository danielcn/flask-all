import smtplib
from email.mime.text import MIMEText

PORT = 2525
SMTP_SERVER = 'smtp.mailtrap.io'

def send_mail(message):
    login = ''
    password = ''
    message = f"<h3>New Feedback Submission</h3><ul><li>Message: {customer}</li></ul>"

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP(SMTP_SERVER, PORT) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
