from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import  ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
# Create your views here.

# class StudentList(ListAPIView):
#     #filter
#     # queryset = Student.objects.filter(passby='user1')
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get_queryset(self):
#         #user having is having current user
#         user = self.request.user
#         return Student.objects.filter(passby=user)

#for restapi filter
# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     #locally declared for per view
#     # filter_backends = [DjangoFilterBackend]
#     #
#     # filterset_fields =['name','city']
#
#     #for search
#     filter_backends = [SearchFilter]
#     # search_fields=['city']
#     #this is search with name or city both or only one
#     # search_fields=['name','city']
#
#     #'^' start with any 1 alpha like search=a
#     search_fields=['^name']
#     #'=' means exact name with complete spell
#     # search_fields = ['=name']


#for orderring
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    filter_backends = [OrderingFilter]
    # ordering_fields=['-name']
    ordering_fields=['name', 'city']