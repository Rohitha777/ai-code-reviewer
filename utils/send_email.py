import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(receiver_email, report_text):
    sender_email = "rohithaandey@gmail.com"
    app_password = "aqdyvpyledhqppzb"  

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Your AI Code Review Report"

    message.attach(MIMEText(report_text, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return True
    except Exception as e:
        return str(e)
