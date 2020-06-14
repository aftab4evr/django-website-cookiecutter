from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed


from django.contrib.gis.geoip2 import GeoIP2

from website.models import (LogHistory,)


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    try:
        ip = request.META.get('REMOTE_ADDR')
        geoip = GeoIP2()
        response = geoip.city(ip)
        LogHistory.objects.create(
            user=user, status='Login', ip=ip, city=response['city'],
            country=response['country_name'], extra=response
        )
    except Exception as e:
        print(e)


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
    try:
        ip = request.META.get('REMOTE_ADDR')
        geoip = GeoIP2()
        response = geoip.city(ip)
        LogHistory.objects.create(
            user=user, status='Logout', ip=ip, city=response['city'],
            country=response['country_name'], extra=response
        )
    except Exception as e:
        print(e)
