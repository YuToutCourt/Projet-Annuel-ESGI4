import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, redirect, url_for, request
from icecream import ic

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/mail', methods=['POST'])
def mail():
    
    if request.method != 'POST':
        return "Method not allowed", 405
    
    subject = request.form['subject']
    mail_from = request.form['email']
    message = request.form['message']
    rcpt_to = "contactbanque@snctf.fr"

    try:
        # Configuration du serveur SMTP
        smtp_server = 'localhost'
        smtp_port = 25

        msg = MIMEMultipart()
        msg['From'] = mail_from
        msg['To'] = rcpt_to
        msg['Subject'] = subject
        msg.attach(MIMEText('\n'.join(message.replace('\r', '\n').split('\n')), 'plain'))

        # Connexion au serveur SMTP et envoi du mail
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.sendmail(mail_from, rcpt_to, msg.as_string())

        return 'Email sent successfully!', 200
    except Exception as e:
        return f'Failed to send email: {str(e)}', 500


if __name__ == '__main__':
    app.run(debug=False, port=8080, host='0.0.0.0')