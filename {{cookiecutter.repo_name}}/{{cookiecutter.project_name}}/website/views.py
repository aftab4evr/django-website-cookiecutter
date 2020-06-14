import json
import datetime
from datetime import datetime, timedelta

from django.db.models import Q
from django.conf import settings
from django.urls import reverse
from django.db.models import Count
from django.views.generic import View
from django.utils.dateparse import parse_datetime
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse

from website.models import (MyUser, Country)
from website.signals import (user_logged_in_callback, user_logged_out_callback)


class LoginView(View):
    def get(self, request):
        return HttpResponse('Login')

    def post(self, request):
        user = authenticate(
            email=request.POST.get('email'),
            password=request.POST.get('password')
        )
        if user is not None:
            login(request, user)
            return redirect("website:dashboard")
        return render(request, 'login.html', {'failureMessage': "Please enter a valid email or password.", })


class ForgotPasswordView(View):
    def get(self, request):
        return render(request, 'forgot-password.html')

    def post(self, request):
        try:
            user = MyUser.objects.get(email=request.POST.get('email'))
            # TODO wite code for send otp or link
            return redirect('website:forgot-link',)
        except MyUser.DoesNotExist:
            return render(request, 'forgot-password.html', {'failure_mesaage': 'This email id is not associate with {{ cookiecutter.project_name }}.'})


@method_decorator(login_required, name='dispatch')
class ChangePasswordView(View):
    def get(self, request):
        return render(request, 'change-password.html')

    def post(self, request):
        if request.POST.get('new_password') == request.POST.get('confirm_password'):
            if request.POST.get('new_password') != request.POST.get('old_passsword'):
                user = MyUser.objects.get(uuid=request.user.uuid)
                if user.check_password(request.POST.get('old_password')):
                    user.set_password(request.POST.get('new_password'))
                    user.save()
                    return redirect('website:login')
                return render(request, 'change-password.html', {'failure_mesaage': 'Invalid old password please enter right password.'})
            return render(request, 'change-password.html', {'failure_mesaage': "New password and old password can't be same."})
        return render(request, 'change-password.html', {'failure_mesaage': 'Password and confirm password miss matched.'})


@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('website:login')
