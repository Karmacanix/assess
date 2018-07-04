from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
import requests

from home.forms import HelpForm

# Create your views here.
def home(request):	
	return render(request, 'home.html')


def guides(request):	
	return render(request, 'guides.html')


def help(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = HelpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
        	email_from = form.cleaned_data['email_from']
        	comments = form.cleaned_data['comments']
        	name = form.cleaned_data['name']
        	message = name + ": " + email_from + ": " + comments
        	sender = 'dhrigby@gmail.com'
        	recipients = ['dhrigby@gmail.com']
        	subject = 'App Acreditation Service Help Request'
        	send_mail(subject, message, sender, recipients)
        	messages.add_message(
    			request, messages.SUCCESS, 'Message sent successfully.',
    			fail_silently=True,
			)
        	return HttpResponseRedirect('/help/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = HelpForm()
        return render(request, 'help.html', {'form': form})