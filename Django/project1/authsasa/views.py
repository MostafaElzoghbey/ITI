from django.shortcuts import render
from django.http import HttpResponse

def mylogin(req):
    
    return render(req, template_name="train/login.html")


def myregistration(req):
    
    return render(req, template_name="train/registration.html")