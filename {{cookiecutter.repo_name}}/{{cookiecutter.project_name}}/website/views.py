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


class Login(View):
    def get(self, request):
        return HttpResponse('Login')


class ForgotPassword(View):
    def get(self, request):
        return HttpResponse('ForgotPassword')
