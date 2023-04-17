
from rest_framework import serializers
from .models import *



class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = weather
        fields = "__all__"
