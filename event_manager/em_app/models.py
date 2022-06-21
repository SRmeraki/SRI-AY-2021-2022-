# from http import client
# import imp
from urllib import response
from django.db import models
from django.db.models.deletion import CASCADE
from django.http import HttpResponse

import environ
from pathlib import Path
import os
# from twilio.rest import Client
# # Initialise environment variables
# env = environ.Env()
# environ.Env.read_env()


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    poster_link = models.URLField( max_length=200)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    register_deadline = models.DateTimeField(auto_now=False, auto_now_add=False)
    host_email = models.EmailField(max_length=254)
    password = models.CharField(max_length=32, default="")

class Participant(models.Model):
    # types = {
    #     ('SING','INDIVIDUAL'),
    #     ('GRP','GROUP'),
    # }
    participant_name = models.CharField(max_length=30,default="")
    contact_no = models.BigIntegerField()    
    participant_email = models.EmailField(max_length=254)
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_type = models.CharField(max_length=50)
    num_of_ppl = models.IntegerField(default=1)

    # using twilio
    
        # to = '{participant.contact_no}'
        # client = twilio.rest.TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        # response = client.messages.create(
        #     body='',
        #     to=to, from_ =settings.TWILIO_PHONE_NUMBER)
    