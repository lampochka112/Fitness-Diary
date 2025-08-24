import os
from celery import Celery
from django.conf import settings
from django.core.mail import send_mail

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_diary.settings')

app = Celery('fitness_diary')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task
def send_daily_reminder(user_email, username):
    subject = 'Напоминание о дневнике питания'
    message = f'Привет, {username}! Не забудь внести свои приемы пищи и тренировки за сегодня!'
    send_mail(subject, message, 'noreply@fitnessdiary.com', [user_email])