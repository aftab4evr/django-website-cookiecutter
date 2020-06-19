import jwt
import uuid
import pyotp
import datetime

from twilio.rest import Client


from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

from website.choice import (USERTYPE, LOGINACTIVITY)


class AbstractTime(models.Model):
    created_at = models.DateTimeField("Created Date", auto_now_add=True)
    updated_at = models.DateTimeField("Updated Date", auto_now=True)

    class Meta:
        abstract = True


class Country(models.Model):
    code = models.CharField('Code', max_length=256,)
    name = models.CharField('Country Name', max_length=256,)


class AccountMangement(BaseUserManager):
    def create_user(self, email, mobile, password, first_name, last_name):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an Email Address')
        if not mobile:
            raise ValueError('Users must have an mobile no')

        user = self.model(
            email=self.normalize_email(email),
            mobile=mobile,
            is_active=False,
            last_name=last_name,
            first_name=first_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mobile, password, first_name, last_name):
        user = self.model(
            email=email,
            mobile=mobile,
            last_name=last_name,
            first_name=first_name
        )
        user.set_password(password)
        user.is_superuser = True
        user.user_type = "Super Admin"
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, AbstractTime):
    code = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, related_name='country_code')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    first_name = models.CharField(_('First name'), max_length=50, blank=True)
    last_name = models.CharField(_('Last name'), max_length=50, blank=True)
    email = models.EmailField(_('Email address'), null=True, unique=True, blank=True, error_messages={
                              'unique': "This email id is already registered."})
    mobile = models.CharField('Mobile Number', max_length=256, null=True, unique=True, blank=True,
                              error_messages={'unique': "This mobile id is already registered."})
    user_type = models.CharField(
        "User Type", max_length=20, default='User', choices=USERTYPE)

    image = models.FileField(
        upload_to='profile/%Y-%M-%d/', null=True, blank=True)
    otp = models.CharField('OTP', max_length=4, blank=True, null=True)
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_(
        'Designates whether the user can log into this admin site.'), )
    is_active = models.BooleanField(_('active'), default=False, help_text=_(
        'Designates whether this user should be treated as active.'), )
    is_otp_verify = models.BooleanField("OTP Verify", default=False)
    is_superuser = models.BooleanField("Super User", default=False)
    is_user_verified = models.BooleanField(default=False)

    objects = AccountMangement()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Account')
        ordering = ['-pk']

    def __str__(self):
        return self.email

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = "{} {}".format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name.strip()

    def sent_otp(self):
        try:
            message = "Thank You! for Signup with FRC. Please use this {} OTP to Verify your mobile number .".format(
                self.otp
            )
            client = Client(
                settings.TWILIO_ACCOUNT_STD,
                settings.TWILIO_AUTH_TOKEN
            )
            code = self.code.code if self.code else '+91'
            message = client.messages.create(
                to=code + self.mobile,
                from_='+15108170600',
                body=message
            )
        except Exception as e:
            print("Exception as e", e)


class UserManagement(AbstractTime):
    '''
        Model for User Management
    '''
    user = models.OneToOneField(
        Account, on_delete=models.CASCADE, related_name='user')
    first_name = models.CharField(
        'First Name', max_length=256, null=True, blank=True,)
    last_name = models.CharField(
        'Last Name', max_length=256, null=True, blank=True,)

    class Meta:
        verbose_name = _('UserManagement')
        verbose_name_plural = _('UserManagement')
        ordering = ['-pk']

    def __str__(self):
        return str(self.user.email)


class LogHistory(AbstractTime):
    user = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="user_log_history")
    status = models.CharField(
        "Status", max_length=20, default='Login', choices=LOGINACTIVITY)
    ip = models.GenericIPAddressField(null=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    extra = JSONField()

    def __str__(self):
        """
        :return: BodyPart
        """
        return str(self.user.email)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Login History"
        ordering = ("-created_at",)
