from urllib import response
from django.shortcuts import render
from django.core.checks import messages
from django.conf import settings
from django.http.response import HttpResponse
# from django_twilio.client import twilio_client
# import twilio.rest
from twilio.rest import Client

from django.core.mail import send_mail
from .models import Event, Participant
from datetime import datetime
import os
import smtplib, ssl
from email.message import EmailMessage


import environ
env = environ.Env()
environ.Env.read_env()

# Create your views here.
def home(request):
    return render(request, 'home.html')

def event_registration(request):
    if request.method =="POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        poster_link = request.POST.get('poster_link')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        register_deadline = request.POST.get('register_deadline')
        host_email = request.POST.get('host_email')
        password = request.POST.get('password')


        if(Event.objects.all().filter(name=name).exists()):
            context = {'messages': "This event name exists already."}
            return render(request, 'event_register.html', context)

        if(Event.objects.all().filter(name=name,description=description, poster_link=poster_link, start_date=start_date, end_date=end_date, register_deadline=register_deadline, host_email=host_email, password=password).exists()):
            context = {'messages': "The event already exists."}
            return render(request, 'event_register.html', context)

        if(start_date > end_date):
            context = {'messages': "Recheck the Start time or End time entry."}
            return render(request, 'event_register.html', context)

        event = Event(name=name, description=description, poster_link=poster_link, start_date=start_date, end_date=end_date, register_deadline=register_deadline, host_email=host_email, password=password)
        event.save() # to save the object instance in the database
        a=event.host_email
        y=event.name
        # send event registration details mail to the host, use SMTP 

        # id = Event.objects.filter(name=event.name).values_list('id',flat=True).first()
        x = Event.objects.all().filter(name=y).first()
        
        content= f"""
        Your Registered Event Details: 
        Event name: {(event.name)}
        Event ID: {(x.id)}
        Description: {(event.description)}
        Event Dates: {(event.start_date)} to {(event.end_date)}
        Registration Deadline: {(event.register_deadline)}
        Email_id: {(event.host_email)}
        Event Password: {(event.password)}        
        """
##############################################################
############### SMTP SERVICE  #############################

        # msg = EmailMessage()
        # msg.set_content(content)
        # msg["Subject"] = "Event Registration Details"
        # msg["From"] = os.environ.get('EMAIL_HOST_USER')
        # msg["To"] = a
        # context=ssl.create_default_context()

        # with smtplib.SMTP('smtp.gmail.com', port=587) as smtp:
        #     smtp.starttls(context=context)
        #     smtp.login(msg["From"], os.environ.get('EMAIL_HOST_PASSWORD'))
        #     smtp.send_message(msg)

#######################################################################################
        # send_mail(
        #     'Event Registration Details', #mail subject
        #     content, #the content to be sent
        #     os.environ.get('EMAIL_HOST_USER'), #sender's email
        #     [host_email], #receiver's email

        # )
        
        context = {'done': "Event registered successfully !"}
        return render(request, 'event_register.html', context)
    return render(request, 'event_register.html')


def participant_registration(request):
    if request.method == 'POST':
        participant_name = request.POST.get('participant_name')
        contact_no = request.POST.get('contact_no')
        participant_email = request.POST.get('participant_email')
        event_name = request.POST.get('event_name')
        registration_type = request.POST.get('registration_type')
        num_of_ppl = request.POST.get('num_of_ppl')
        # if(registration_type=='INDIVIDUAL'):
        #     num_of_ppl = 1

        # if(registration_type=='GROUP'):
        #     num_of_ppl = request.POST.get('num_of_ppl')    


        eve = Event.objects.all().filter(name=event_name).first()   

        # Already Registered
        if Participant.objects.all().filter(participant_name=participant_name, contact_no=contact_no,participant_email=participant_email,event_name=eve):
            context = {'messages':"This participant is already registered in the event !",'show_events': Event.objects.all().filter(register_deadline__gte=datetime.now())}
            return render(request, 'participant_register.html', context)

        
        # New participant object
        participant = Participant(participant_name=participant_name, contact_no=contact_no, participant_email=participant_email, event_name=eve, registration_type=registration_type, num_of_ppl=num_of_ppl)
        participant.save()
        y = Participant.objects.all().filter(participant_name=participant.participant_name).first()

        # to = participant.contact_no

        # i = participant.participant_name
        # j = participant.contact_no
        # Participant's Unique ID: {(y.id)}
        # x = Event.objects.all().filter(name=j).first()
        # 
        content= f"""
        Participant's ID: {(y.id)}
        Event Name: {(eve.name)}
        Description: {(eve.description)}
        Event Dates: {(eve.start_date)} to {(eve.end_date)}
        Host's Email_id: {(eve.host_email)}
        """

        print(content)
# ##############################################################
        # TWILIO SMS SERVICE ####################################   
         
        # def send_twilio_mssg():
        #     TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
        #     TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
        #     TWILIO_PHONE_NUMBER= os.environ.get('TWILIO_PHONE_NUMBER')
        #     TWILIO_PHONE_NUMBER_2= os.environ.get('TWILIO_PHONE_NUMBER_2')
        #     body = f"""
        #     Participant's ID: {(y.id)}
        #     Event Name: {(eve.name)}
        #     Description: {(eve.description)}
        #     Event Dates: {(eve.start_date)} to {(eve.end_date)}
        #     Host's Email_id: {(eve.host_email)}
        #     """
        #     client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
        #     response = client.messages.create(
        #         body=body,
        #         from_=TWILIO_PHONE_NUMBER,
        #         to=TWILIO_PHONE_NUMBER_2
        #     )

        #     print(response.sid)

        # send_twilio_mssg()

###############################################
        
        
# to show the event details to the registered participant
    context = {'show_events': Event.objects.all().filter(register_deadline__gte=datetime.now())} #to show details of only the upcoming event and not those which alredy passed
    return render(request, 'participant_register.html', context)

def event_dashboard(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        password = request.POST.get('password')
        host_email = request.POST.get('host_email')

        
        if  (Event.objects.all().filter(id=event_id).exists() and Event.objects.get(id=event_id).password == password) and Event.objects.get(id=event_id).host_email == host_email :
            context = {'messages':"Participants' List Below",'participants_list': Participant.objects.all().filter(event_name=event_id)}
            return render(request, 'event_dashboard.html',context) 
        else:
            context = {'messages':"Event_ID or password or Host's Email is incorrect !"}
            return render(request, 'event_dashboard.html', context)
    return render(request, 'event_dashboard.html')