"""
URL configuration for lab02 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from trainee.views import *
from authsasa.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("register",Register,name="Register"),
    
    path("listUsers",ListUsers,name="ListUsers"),
    
    path('List_Trainee',listTrainee,name='Listtrainee'),
    path('Insert_Trainee',InsertTrainee,name='InsertTrainee'),
    path('Update_Trainee/<int:ID>',Update_Trainee,name='Update_Trainee'),
    path('Delete_Trainee/<int:ID>',Delete_Trainee,name='Delete_Trainee'),
    
    path('api/all',all_trainee,),
    path('api/add',add_trainee,),
    path('api/delete/<int:ID>',delete_trainee,),
    path('api/update/<int:ID>',update_trainee,),
]
