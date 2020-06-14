from tqdm import tqdm
import time
import sys
import os
import json

from django.core.management.base import BaseCommand

from website.models import Country
from staticcontent.models import (PrivacyPolicy, AboutUs, TermsConditions)


def load_country_data():
    with open('json/country.json') as f:
        count = 0
        print("Uploading Country code please wait it will take some time......\n")
        for item in json.load(f):
            count += 1
            Country.objects.get_or_create(
                country_code=item['dial_code'],
                name=item['name']
            )
            for i in tqdm(range(count)):
                time.sleep(0.005)
        print("\nCountry Code addeed successfully: ", count)


def privacy_policy_load():
    with open('json/privacy-policy.json') as f:
        data = json.load(f)
        instance = PrivacyPolicy.objects.all().last()
        if instance:
            instance.title = data['title']
            instance.description = data['description']
            instance.save()
        else:
            PrivacyPolicy.objects.create(
                title=data['title'],
                description=data['description'],
            )
        for i in tqdm(range(0, 1)):
            time.sleep(0.1)


def terms_conditions():
    with open('json/termsandonditions.json') as f:
        data = json.load(f)
        instance = TermsConditions.objects.all().last()
        if instance:
            instance.title = data['title']
            instance.description = data['description']
            instance.save()
        else:
            TermsConditions.objects.create(
                title=data['title'],
                description=data['description'],
            )
    for i in tqdm(range(0, 1)):
        time.sleep(0.1)


def about_us():
    with open('json/about-us.json') as f:
        data = json.load(f)
        instance = AboutUs.objects.all().last()
        if instance:
            instance.title = data['title']
            instance.description = data['description']
            instance.save()
        else:
            AboutUs.objects.create(
                title=data['title'],
                description=data['description'],
            )
    for i in tqdm(range(0, 1)):
        time.sleep(0.1)


class Command(BaseCommand):
    help = 'Loading data into Database'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file_name', type=str,
                            help='Write files name.')

    def handle(self, *args, **kwargs):
        if kwargs['file_name'] == 'country':
            load_country_data()

        elif kwargs['file_name'] == 'privacypolicy':
            privacy_policy_load()
        elif kwargs['file_name'] == 'doctorterms':
            terms_conditions()
        elif kwargs['file_name'] == 'all':
            load_country_data()
            privacy_policy_load()
            terms_conditions()
        else:
            print(
                "Invalid file name.\nplease specifies files in \n['country','cities' , 'specialization','disease','noofpatientvisitdaily','permission' or 'all']")
