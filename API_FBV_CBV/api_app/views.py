from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
@api_view()
def helloworld(request):
    return Response({'msg':'hello world'})

@api_view(['GET','POST'])
def helloworld(request):
    if request.method =='GET':
        return Response({'msg':'This is GET request'})

    if request.method =='POST':
     print(request.data)
    return Response({'msg':'This is PoST request','data': request.data})


#function based API views

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def Student_api(request,pk=None):
    if request.method == 'GET':
        id=pk
        # id=request.data.get('id')
        print(id)
        if id is not None:
          stu=Student.objects.get(pk=id)
          print(stu)
          serializer = StudentSerializer(stu)
          print(serializer)
          print(serializer.data)
          return Response(serializer.data)
        else:
            stu=Student.objects.all()
            serializer=StudentSerializer(stu, many=True)
            return Response(serializer.data)

    if request.method =='POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'PUT':
        # id=request.data.get('id')
        id=pk
        stu=Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated successfully'})
        else:
            return Response(serializer.errors)

    if request.method == "PATCH":
        # id=pk
        stu=Student.objects.get(id=pk)
        serializer=StudentSerializer(stu,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data updated'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    if request.method =='DELETE':
        # id=request.data.get('id')
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data deleted'})
    else:
        return Response({'msg':'Data does not exixts'})

#class based API view

class StudentAPI(APIView):
    def get(self,request,pk=None,format=None):
        if id is not None:
            stu=Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu=Student.objects.all()
            serializer=StudentSerializer(stu, many=True)
            return Response(serializer.data)

    def post(self,request,format=None):
        serilaizer = StudentSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serilaizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk,format=None,):
        stu=Student.objects.get(id=pk)
        serializer=StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data updated'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk,format=None):
        stu=Student.objects.get(id=pk)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial data updated'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None,pk=None):
        stu=Student.objects.get(id=pk)
        stu.delete()
        return Response({'msg':'data deleted successfully'})

#GenericAPIView and mixin(ModelMixin)
class StudentList(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class StudentCreate(CreateModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class StudentReterive(RetrieveModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args, **kwargs)

class StudentUpdate(UpdateModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def put(self,request, *args, **kwargs):
        return self.update(request,*args, **kwargs)

class StudentDelete(DestroyModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args,*kwargs)


#list and create pk not require
class Student_List_Ceate_API(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# retrieve, Update and Destroy pk required
class Student_Retrieve_Update_Delete_API(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self,request, *args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args,*kwargs)

#concrete view class which extends from generics and mixins
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class Student_List_Create(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Student_Retrieve_Update(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Student_Retrieve_Destroy(RetrieveDestroyAPIView):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer

class Student_Ret_Upd_Des(RetrieveUpdateDestroyAPIView):
            queryset = Student.objects.all()
            serializer_class = StudentSerializer

















