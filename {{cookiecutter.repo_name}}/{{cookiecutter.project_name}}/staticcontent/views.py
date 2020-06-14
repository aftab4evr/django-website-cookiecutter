from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse

from staticcontent.models import (AboutUs, ContactUs,TermsConditions,PrivacyPolicy)


class AboutUsView(View):
    def get(self, request):
        return render(request,'static-content/about-us.html')


class ContactUsView(View):
    def get(self, request):
        return render(request,'static-content/contact-us.html')

class TermsConditionsView(View):
    def get(self, request):
        return render(request,'static-content/terms-conditions.html')

class PrivacyPolicyView(View):
    def get(self, request):
        return render(request,'static-content/privacy-policy.html')