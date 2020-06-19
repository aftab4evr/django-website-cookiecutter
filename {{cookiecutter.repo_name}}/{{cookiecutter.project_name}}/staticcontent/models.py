from django.db import models
from website.models import AbstractTime, Account


class TermsConditions(AbstractTime):
    title = models.CharField('Title', max_length=255, blank=True, null=True)
    description = models.TextField('Description', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Terms and Conditions"


class PrivacyPolicy(AbstractTime):
    title = models.CharField('Title', max_length=255, blank=True, null=True)
    description = models.TextField('Description', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Privacy Policy"


class AboutUs(AbstractTime):
    title = models.CharField('Title', max_length=255, blank=True, null=True)
    description = models.TextField('Description', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About Us"


class ContactUs(AbstractTime):
    user = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="contact_user")
    name = models.CharField(
        "Name", max_length=256, null=True, blank=True)
    mobile = models.CharField(
        'Mobile', max_length=256, blank=True, null=True)
    email = models.EmailField(
        "Email", blank=True, null=True)
    message = models.TextField(
        "Message", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Us"
