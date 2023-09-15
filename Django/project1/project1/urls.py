"""
URL configuration for project1 project.

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
from django.urls import include, path
from trainee.views import *
from instructor.views import *
from authsasa.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('app1.urls')),
    # path('', include('trainee.urls')),
    path('home', Home, name='home'),
    path('', Index, name='index'),
    
    path('trainee/', trhome, name='trhome'),
    path('trainee/list_trainee/', listTrainee, name='trlist'),
    path('trainee/insert_trainee/', insertTrainee, name='trinsert'),
    path('trainee/update_trainee/', updateTrainee, name='trupdate'),
    path('trainee/delete_trainee/', deleteTrainee, name='trdelete'),
    
    path('instructor/', insthome, name='insthome'),
    path('instructor/list_instructor/', listInstructor, name='instlist'),
    path('instructor/insert_instructor/', insertInstructor, name='instinsert'),
    path('instructor/update_instructor/', updateInstructor, name='instupdate'),
    path('instructor/delete_instructor/', deleteInstructor, name='instdelete'),
    
    path('login', mylogin, name='login'),
    path('registration', myregistration, name='registration'),
]
