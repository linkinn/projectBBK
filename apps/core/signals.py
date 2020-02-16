from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from apps.core.models import LogsLogin
import logging
import time

logger = logging.getLogger('login')


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    logger.info(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - Login User: {user} - IP: {ip}')
    LogsLogin.objects.create(user=user, type='Login', ip=ip)


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    logger.info(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - Logout user: {user} - IP {ip}')
    LogsLogin.objects.create(user=user, type='Logout', ip=ip)


@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, **kwargs):
    user = credentials['username']
    logger.warning(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - Login failed for: {user}')
    LogsLogin.objects.create(user=user, type='Login Failed')
