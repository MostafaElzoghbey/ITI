from  django import  forms
from .models import Trainee,Track

class Newtraineeform(forms.ModelForm):
    class Meta:
        model=Trainee
        fields='__all__'