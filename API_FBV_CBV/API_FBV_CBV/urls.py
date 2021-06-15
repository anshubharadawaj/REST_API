"""API_FBV_CBV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_fbv/',views.helloworld),

    #for fbv
    path('student_api_fbv/',views.Student_api),
    path('student_api_fbv/<int:pk>/',views.Student_api),

    #for cbv
    path('student_api_cbv/',views.StudentAPI.as_view()),
    path('student_api_cbv/<int:pk>/',views.StudentAPI.as_view()),

    #for generic and mixin
    # path('student_api/', views.StudentList.as_view()),
    # path('student_api/', views.StudentCreate.as_view()),
    # path('student_api/<int:pk>/', views.StudentReterive.as_view()),
    # path('student_api/<int:pk>/', views.StudentUpdate.as_view()),
    # path('student_api/<int:pk>/', views.StudentDelete.as_view()),

    #for list and create pk not required in geneic and mixin
    # path('student_api/', views.Student_List_Ceate_API.as_view()),
    # path('student_api/<int:pk>/', views.Student_Retrieve_Update_Delete_API.as_view()),

    #concrete API VIEW
    # path('student_api/', views.StudentList.as_view()),
    # path('student_api/', views.StudentCreate.as_view()),
    # path('student_api/<int:pk>/', views.StudentReterive.as_view()),
    # path('student_api/<int:pk>/', views.StudentUpdate.as_view()),
    # path('student_api/<int:pk>/', views.StudentDelete.as_view()),

    # path('student_api/', views.Student_List_Create.as_view()),
    # path('student_api/<int:pk>/', views.Student_Retrieve_Update.as_view()),
    # path('student_api/<int:pk>/', views.Student_Retrieve_Destroy.as_view()),
    # path('student_api/<int:pk>/', views.Student_Ret_Upd_Des.as_view()),

    # path('student_api/', views.Student_List_Create.as_view()),
    # path('student_api/<int:pk>/', views.Student_Ret_Upd_Des.as_view()),




 ]
