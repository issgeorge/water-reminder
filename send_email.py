import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Get environment variables from GitHub Secrets
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

# List of catchy phrases
catchy_phrases = [
    "Stay Hydrated, Stay Healthy!",
    "Water: Your Brain’s Best Friend!",
    "Drink Water, Keep Going!",
    "Hydration = Happiness!",
    "Sip, Sip, Hooray! Drink Water Now!"
]

# Choose a random phrase
subject = random.choice(catchy_phrases)
body = "Hey there!\n\nJust a friendly reminder to drink some water and stay hydrated!\n\nCheers!"

# Email setup
msg = MIMEMultipart()
msg["From"] = EMAIL_SENDER
msg["To"] = EMAIL_RECEIVER
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

# Sending email
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)
    server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
