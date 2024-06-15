from celery import shared_task
from django.utils import timezone

from .models import User

@shared_task
def reset_strike_status():
    # Находим записи, где strike_status равно True и обновляем их на False
    User.objects.filter(strike_status=True).update(strike_status=False)

@shared_task
def reset_strike():
    today = timezone.now().date()
    users = User.objects.filter(last_lesson_date__lt=today)
    for user in users:
        user.strike = 0
        user.save()

@shared_task()
def reset_week_rating():
    users = User.object.all()
    for user in users:
        user.week_rating = 0
        user.save()
