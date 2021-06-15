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

#for token authentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token



# class EmployeeModelViewSet(viewsets.ModelViewSet):
#
#         queryset = Employee.objects.all()
#         serializer_class = EmployeeSerializer
#         authentication_classes = [TokenAuthentication]
#         permission_classes = [IsAuthenticated]
        # authentication_classes = [BasicAuthentication]
        # authentication_classes = [SessionAuthentication]

        # permission_classes = [AllowAny]
        # permission_classes = [IsAdminUser]
        # permission_classes=[IsAuthenticatedOrReadOnly]
        # permission_classes = [DjangoModelPermissions]
        # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
        # permission_classes = [MyPermission]


#function based API views

@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def Employee_api(request,pk=None):
    if request.method == 'GET':
        id=pk
        # id=request.data.get('id')
        print(id)
        if id is not None:
          stu=Employee.objects.get(pk=id)
          print(stu)
          serializer = EmployeeSerializer(stu)
          print(serializer)
          print(serializer.data)
          return Response(serializer.data)
        else:
            stu=Employee.objects.all()
            serializer=EmployeeSerializer(stu, many=True)
            return Response(serializer.data)

    if request.method =='POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'PUT':
        # id=request.data.get('id')
        id=pk
        stu=Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated successfully'})
        else:
            return Response(serializer.errors)

    if request.method == "PATCH":
        # id=pk
        stu=Employee.objects.get(id=pk)
        serializer=EmployeeSerializer(stu,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data updated'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    if request.method =='DELETE':
        # id=request.data.get('id')
        id=pk
        stu=Employee.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data deleted'})
    else:
        return Response({'msg':'Data does not exixts'})

#token based Authentication

class EmployeeModelViewSet(viewsets.ModelViewSet):

        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer


class CustomAuthToken(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        if serializer.is_valid(raise_exception=True):
            user=serializer.validated_data['user']
            token,created=Token.objects.get_or_create(user=user)
            return Response({
                'token':token.key,
                'user_id':user.pk,
                'user_email':user.email

            })

#Custom Authentication
class EmployeeModelViewSet(viewsets.ModelViewSet):

        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer
        authentication_classes=[CustomAuthentication]
        permission_classes = [IsAuthenticated]

