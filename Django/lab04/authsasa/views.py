from django.shortcuts import render
from .models import Myaccount


def ListUsers(req):
    
    users=Myaccount.objects.all()
    context={'users':users}
    
    return render(req, 'ListUsers.html',context)

def Register(request):
    
    # username = request.POST.get('Username', '') 
    # password = request.POST.get('Password', '') 
    if (request.method == 'POST'):
        
        # username = request.POST('Username') 
        # password = request.POST('Password')
        username = request.POST.get('Username')
        password = request.POST.get('Password')
    
        Myaccount.objects.create(username=username, password=password)
    
    return  render(request,'Register.html')
