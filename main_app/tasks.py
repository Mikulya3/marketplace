from main_app.celery import app
from django.core.mail import send_mail

@app.task
def spam_message():
    send_mail(
        'hi, we are from Marketplace SpaceX',
        'we want to offer some new products and discounts on NEW Year Products!!!'
        'kadirbekova43@gmail.com',
        ['kadirbekova43@gmail.com'],
    )