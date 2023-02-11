import datetime

from celery import shared_task
from celery.utils.log import get_task_logger
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models import Q

from .models import Availability

logger = get_task_logger(__name__)


@shared_task
def sample_task():
    logger.info("The sample task just ran.")


@shared_task
def send_notifications():
    users = get_user_model().objects.filter(is_active=True)
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    send_to = set()

    for user in users:
        if not user.email:
            continue
        lessons = Availability.objects.filter(
            Q(teacher=user) | Q(student=user))
        for lesson in lessons:
            if lesson.date == tomorrow and lesson.is_booked:
                send_to.add(user)

    for user in send_to:
        print(f"### Mock Sending email to {user.email} ###")
