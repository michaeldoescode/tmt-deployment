import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

import random
from faker import Faker
from AppTwo.models import AccessRecord, Webpage, Topic

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def add_webpage():
    topic = add_topic()
    fake_url = fakegen.url()
    fake_date = fakegen.date()
    fake_name = fakegen.company()

    webpage = Webpage.objects.get_or_create(topic=topic,url=fake_url,name=fake_name)[0]
    return webpage

def add_access_record():
    webpage = add_webpage()
    fake_date = fakegen.date()

    access_record = AccessRecord.objects.get_or_create(name=webpage,date=fake_date)[0]

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    for _ in range(20):
        add_access_record()
    print('Populating Complete')
