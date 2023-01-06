from django.core.mail import send_mail
from applications.spam.models import Spam
from main_app.celery import app

@app.task
def send_spam_message_to_users():
    emails = Spam.objects.all()
    list_email = [i.email for i in emails]
    for email in emails:
        send_mail(
            'hi',
            'this is our site http://localhost:8000',
            'kadirbekova43@gmail.com',
            list_email
        )
