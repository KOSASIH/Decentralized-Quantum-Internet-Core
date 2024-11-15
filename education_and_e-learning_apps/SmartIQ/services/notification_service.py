from flask_mail import Mail, Message

mail = Mail()

class NotificationService:
    @staticmethod
    def send_email(subject, recipient, body):
        msg = Message(subject, recipients=[recipient])
        msg.body = body
        mail.send(msg)
