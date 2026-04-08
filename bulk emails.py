import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tqdm import tqdm
import time

# Your Gmail details
EMAIL = "rishimt2021@gmail.com"
APP_PASSWORD = "ipjkmsndybxxidqu"

# List of people to email
contacts = [
    {"name": "Rishi Rathod", "email": "rishimt2021@gmail.com"},
    {"name": "Test Person", "email": "rishirathod2403@gmail.com"},
    {"name": "Another Person", "email": "rishi.hr@somaiya.edu"},
]


def send_email(to_email, name):
    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = to_email
    msg["Subject"] = f"Hello {name}!"

    body = f"""
Hi {name},

Hope you are doing well!

This is a personalized email sent automatically using Python.

Best regards,
Rishi Rathod
"""
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, APP_PASSWORD)
        server.sendmail(EMAIL, to_email, msg.as_string())


def send_bulk_emails():
    print("Starting bulk email sender...\n")

    successful = 0
    failed = 0

    for contact in tqdm(contacts, desc="Sending emails", ncols=60, colour="green"):
        try:
            send_email(contact["email"], contact["name"])
            successful += 1
            time.sleep(2)  # Wait 2 seconds between emails
        except Exception as e:
            print(f"\n❌ Failed to send to {contact['name']}: {e}")
            failed += 1

    print(f"\n✅ Done!")
    print(f"📧 Successful: {successful}")
    print(f"❌ Failed: {failed}")


send_bulk_emails()