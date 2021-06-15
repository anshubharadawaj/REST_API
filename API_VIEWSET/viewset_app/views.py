from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Employee
from rest_framework import status
from .serializers import EmployeeSerializer



class EmployeeViewSet(viewsets.ViewSet):
    def list(self,request):
            print("********LIST*****")
            print("basename:",self.basename)
            print("action",self.action)
            print("suffix",self.suffix)
            print("details",self.detail)
            print("name", self.name)
            print("description", self.description)
            stu=Employee.objects.all()
            serializer=EmployeeSerializer(stu, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    def retrieve(self,request,pk=None):
            stu = Employee.objects.get(id=pk)
            serializer = EmployeeSerializer(stu)
            return Response(serializer.data)

    def create(self,request):
        serializer =EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created Successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
            stu= Employee.objects.get(id=pk)
            serializer=EmployeeSerializer(stu,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Complete Data updated'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
            stu =Employee.objects.get(id=pk)
            serializer = EmployeeSerializer(stu, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Complete Data updated'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk=None):
        stu=Employee.objects.get(id=pk)
        stu.delete()
        return Response ({'msg':'Data deleted'})


#ModelViewSet
class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


#ReadOnlyModelViewSet
class EmployeeReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


