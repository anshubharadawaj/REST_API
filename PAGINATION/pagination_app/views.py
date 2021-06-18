from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer
# from rest_framework.pagination import PageNumberPagination
# from .mypagination import MyPageNumberPAgination
# from .mypagination import MyLimitOffsetPagination
from .mypagination import MyCursorPagination

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # pagination_class = MyPageNumberPAgination
    # pagination_class = MyLimitOffsetPagination
    pagination_class = MyCursorPagination