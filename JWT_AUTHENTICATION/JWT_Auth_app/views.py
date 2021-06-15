from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from .custompermission import MyPermission
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,DjangoModelPermissionsOrAnonReadOnly,IsAuthenticatedOrReadOnly,DjangoModelPermissions
from .custom_authentication import CustomAuthentication
# Create your views here.

class EmployeeModelViewSet(viewsets.ModelViewSet):

        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer
        authentication_classes=[CustomAuthentication]
        permission_classes = [IsAuthenticated]