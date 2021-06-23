from django.shortcuts import render

# Create your views here.

from .models import Singer,Song
# from .models import Student
# from .serializer import StudentSerializer
from .serializer import SingerSerializer,SongSerializer
from rest_framework import viewsets

class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer



# for hyperlinked view
# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
