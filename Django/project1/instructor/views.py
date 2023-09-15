from django.shortcuts import render

def insthome(req):
    
    return render(req, template_name="Instr/insthome.html")


def listInstructor(req):
    
    return render(req, template_name="Instr/list.html")


def insertInstructor(req):
    
    return render(req, template_name="Instr/insert.html")


def updateInstructor(req):
    
    return render(req, template_name="Instr/update.html")


def deleteInstructor(req):
    
    return render(req, template_name="Instr/delete.html")
