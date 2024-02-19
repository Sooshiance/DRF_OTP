from celery import shared_task
from django.utils.timezone import timedelta, datetime 


@shared_task
def deleteOTP(user):
    pass    
