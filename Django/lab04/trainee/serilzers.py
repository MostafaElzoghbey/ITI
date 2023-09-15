from rest_framework import serializers
from .models import Trainee, Track


class Trackserlizer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Track
        fields = ['id', 'name']
        

class Traineeserlizer(serializers.ModelSerializer):
    
    track = Trackserlizer(read_only=True)
    track_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        
        model = Trainee
        fields = ['id', 'name', 'track', 'track_id']