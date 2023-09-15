from django.shortcuts import render
from django.http import HttpResponse


def Index(req):
    
    return render(req, template_name="index.html")


def Home(req):
    
    return render(req, template_name="home.html")

def trhome(req):
    
    return render(req, template_name="train/trhome.html")


def listTrainee(req):
    
    return render(req, template_name="train/list.html")


def insertTrainee(req):
    
    return render(req, template_name="train/insert.html")


def updateTrainee(req):
    
    return render(req, template_name="train/update.html")


def deleteTrainee(req):
    
    return render(req, template_name="train/delete.html")