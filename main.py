from flask import Flask, request, jsonify, render_template
import smtplib
from email.message import EmailMessage
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()  

app = Flask(__name__)

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Route for homepage
@app.route("/")
def home():
    current_year = datetime.now().year
    return render_template('index.html', year=current_year)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    name = data.get('name')
    sender_email = data.get('email')
    message = data.get('message')

    EMAIL_ADDRESS = 'mohammadbagheri07@gmail.com'
    EMAIL_PASSWORD = 'aufb mwji ener rpqj'  

    msg = EmailMessage()
    msg['Subject'] = f'Contact from {name}'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content(f"From: {name}\nEmail: {sender_email}\n\nMessage:\n{message}")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return jsonify({'message': 'Email sent successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
