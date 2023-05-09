from send_email.celery import app
from .service import send
from .models import Contact
from django.core.mail import send_mail


@app.task
def send_spam_email(user_email):
    send(user_email)


# @app.task
# def send_beat_email():
#     for contact in Contact.objects.all():
#         send_mail(
#             'Вы подписались на рассылку',
#             'Мы будем присылать много спама',
#             'tt8338931@gmail.com',
#             [contact.email],
#             fail_silently=False,
#         )