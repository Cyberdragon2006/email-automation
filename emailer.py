import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your Gmail details
EMAIL = "rishimt2021@gmail.com"
APP_PASSWORD = "ipjkmsndybxxidqu"


def send_email(to_email, name):
    # Create email
    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = to_email
    msg["Subject"] = f"Hello {name}!"

    # Email body
    body = f"""
Hi {name},

Hope you are doing well!

This email was sent automatically using Python.

Best regards,
Your Name
"""
    msg.attach(MIMEText(body, "plain"))

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, APP_PASSWORD)
        server.sendmail(EMAIL, to_email, msg.as_string())
        print(f"✅ Email sent to {name} at {to_email}")


# Test - send to yourself first
send_email("rishi mt2021@gmail.com", "Rishi Rathod")