import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
import requests



# Create your views here.
def get_data_weather(data):
    BASE_URL = "https://demo.openweathermap.org/energy/1.0/solar/data?"
    API_KEY = "8f3f3bfa1f66c8879ef015dfb95c801b"
    LAT = str(data['lat'])
    LONG = str(data['long'])
    DATE = str(data['Date'])
    url = BASE_URL + "lat=" + LAT + "&lon=" + LONG + "&date=" + DATE + "&appid=" + API_KEY
    reaponse = requests.get(url).json()
    print(reaponse['irradiance']['daily'])
    return reaponse



class WeatherView(APIView):
    def post(self, request):
        serializer = WeatherSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = get_data_weather(data=serializer.data)
            return Response({'data':data['irradiance']['daily'], 'status': status.HTTP_200_OK})