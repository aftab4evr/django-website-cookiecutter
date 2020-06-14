from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from website.views import (
    Login,
    ForgotPassword,
)

from staticcontent.views import(AboutUsView, ContactUsView, PrivacyPolicyView, TermsConditionsView)

urlpatterns = [

    # Static content
    url(r'^about-us', AboutUsView.as_view(), name="about-us"),
    url(r'^contact-us', ContactUsView.as_view(), name="contact-us"),
    url(r'^privacy-policy', PrivacyPolicy.as_view(), name="privacy-policy"),
    url(r'^terms-condition', TermsConditionsView.as_view(), name="terms-condition"),



    # Pre Auth
    url(r'^$', Login.as_view(), name="login"),
    # url(r'^forgot-password$', ForgotPassword.as_view(), name="forgot-password"),
    # url(r'^reset-password/(?P<uuid>[0-9A-Za-z_\-]+)/(?P<time>[0-9A-Za-z_\-]+)/$',
    #     ResetPassword.as_view(), name="reset-password"),
    # url(r'^forgot-link$', ForgotLink.as_view(), name="forgot-link"),
    # url(r'^link-expire$', LinkExpire.as_view(), name="link-expire"),
    # url(r'^password-changed$', PasswordChanged.as_view(), name="password-changed"),

    # # Post Auth

    # url(r'^dashboard$', Dashboard.as_view(), name="dashboard"),
    # url(r'^profile$', Profile.as_view(), name="profile"),
    # url(r'^change-password$', ChangePassword.as_view(), name="change-password"),

    # url(r'^logout$', Logout.as_view(), name="logout"),


]
