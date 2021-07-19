from django.core.mail import EmailMessage
import threading


class EmailThreading(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    
    def run(self):
        self.email.send()

class Util:
    @staticmethod
    def send_email(data):
        email=EmailMessage(
             subject=data['subject'], body=data['message'], to=[data['to_email']])
        EmailThreading(email).start()