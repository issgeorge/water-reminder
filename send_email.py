import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Get environment variables from GitHub Secrets
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

# Ensure the environment variables are fetched
if not all([EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER]):
    print("❌ Missing environment variables. Please check your secrets.")
    exit(1)

# List of catchy phrases with placeholders for emojis
catchy_phrases = [
    "Vishnuuuuuuu! 💧 Stay Hydrated, Stay Happy! {}",
    "Vishnuuuuuuu! 🚰 Water: Your Brain’s Best Friend! {}",
    "Vishnuuuuuuu! 🕺 Drink Water, Dance Happy! {}",
    "Vishnuuuuuuu! 🌊 Hydration = Happiness! {}",
    "Vishnuuuuuuu! 🥤 Sip, Sip, Hooray! Drink Water Now! {}"
]

# List of smileys and icons to append
emojis = ["😃", "😊", "🤩", "🥤", "💦", "💙", "🔥", "☀️", "🌟", "✨"]

# Choose a random phrase and emoji
subject = random.choice(catchy_phrases).format(random.choice(emojis))
body = "Vishnuuuuuuuuuuuuuuuu!\n\nJust a reminder to drink a glass of water!\n\nCheers! 💧😊"

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
    print("✅ Email sent successfully!")
except Exception as e:
    print(f"❌ Error: {e}")
