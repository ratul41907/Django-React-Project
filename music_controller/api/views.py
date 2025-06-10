from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer  # Assuming RoomSerializer is imported from serializers.py
from .models import Room  # Assuming Room is imported from models.py
class RoomView(generics.CreateAPIView):
    # This view will list all rooms
    queryset = Room.objects.all()  # Assuming Room is imported from models.py
    serializer_class = RoomSerializer  # Assuming RoomSerializer is imported from serializers.py
#from django.http import HttpResponse
# Create your views here.
##   return HttpResponse("<h1>Hello</h1>")