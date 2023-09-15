from  django.http import  HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .form import *


def index(request):
    
    return render(request, 'index.html')


def listTrainee(req):
    
    context={'trainees':Trainee.objects.all()}
    
    return render(req,'ListTrainee.html',context)


def InsertTrainee(req):
    
    form=Newtraineeform()
    context={}
    if(req.method=='POST'):
        
        form=Newtraineeform(req.POST)
        
        if(form.is_valid()):
            
            form.save()
        else:
            context['msg']='enter valid data'
            
    context['form']=form

    return render(req,'traineeinsert.html',context)


def Update_Trainee(req,ID):
    
    train=Trainee.objects.get(id=ID)
    form=Newtraineeform(instance=train)
    if(req.method=='POST'):
        
        f=Newtraineeform(req.POST,instance=train)

        if(f.is_valid()):
            
            f.save()
            return  HttpResponseRedirect('/List_Trainee')
        
    context={'form':form}
    
    return render(req,'updatetrainee.html',context)


def Delete_Trainee(req,ID):
    
    Trainee.objects.get(id=ID).delete()
    
    return HttpResponseRedirect('/List_Trainee')


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serilzers import *

@api_view(['GET'])
def all_trainee(req):
    
    objs = Trainee.objects.all()
    jsndata = Traineeserlizer(objs, many=True).data
    finaldata = {'data': jsndata}

    return Response(data=finaldata, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_trainee(req):
    
    trainee = Traineeserlizer(data=req.data)
    if (trainee.is_valid()):

        trainee.save()

    return Response(status.HTTP_201_CREATED)


@api_view(['DELETE'])
def delete_trainee(req, ID):
    
    Trainee.objects.filter(id=ID).delete()

    return Response(status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_trainee(req, ID):
    
    t = Trainee.objects.filter(id=ID)[0]
    st = Traineeserlizer(instance=t, data=req.data, partial=True)
    
    if (st.is_valid()):
        
        st.save()

    return Response(status.HTTP_200_OK)
