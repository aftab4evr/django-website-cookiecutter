from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from website.views import (
    LoginView, LogoutView,
    ForgotPasswordView,
    ChangePasswordView,
)

from staticcontent.views import(AboutUsView, ContactUsView, PrivacyPolicyView, TermsConditionsView)

urlpatterns = [

    # Static content
    url(r'^about-us', AboutUsView.as_view(), name="about-us"),
    url(r'^contact-us', ContactUsView.as_view(), name="contact-us"),
    url(r'^privacy-policy', PrivacyPolicyView.as_view(), name="privacy-policy"),
    url(r'^terms-condition', TermsConditionsView.as_view(), name="terms-condition"),



    # Pre Auth
    url(r'^$', LoginView.as_view(), name="login"),
    url(r'^forgot-password$', ForgotPasswordView.as_view(), name="forgot-password"),

    # Post Auth
    url(r'^change-password$', ChangePasswordView.as_view(), name="change-password"),
    url(r'^logout$', LogoutView.as_view(), name="logout"),

]
