from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle,ScopedRateThrottle
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from .throttle import JackRateThrottle
# Create your views here.

class EmployeeModelViewSet(viewsets.ModelViewSet):

        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer
        authentication_classes=[SessionAuthentication]
        permission_classes = [IsAuthenticatedOrReadOnly]
        #locally called
        # throttle_classes = [UserRateThrottle,AnonRateThrottle]
        throttle_classes = [JackRateThrottle,AnonRateThrottle]


class EmployeeList(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    throttle_scope ='viewemp'

class EmployeeCreate(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    throttle_scope = 'viewemp'

class EmployeeRetrieve(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    throttle_scope = 'modifyemp'

class EmployeeUpdate(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    throttle_scope = 'modifyemp'

class EmployeeDestroy(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    throttle_scope = 'modifyemp'