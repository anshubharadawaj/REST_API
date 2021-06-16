"""THROTTLING URL Configuration

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
from django.urls import path, include
from Throttling_app import views
from rest_framework.routers import DefaultRouter



#creating  router object
router=DefaultRouter()

#register ViewSet with Router

# router.register('employeeapi',views.EmployeeModelViewSet, basename='employee')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('auth/',include('rest_framework.urls', namespace='rest_framework') ),
    # path('employeeapi/', views.EmployeeList.as_view(), name='employee'),
    # path('employeeapi/', views.EmployeeCreate.as_view(),name='employee'),
    path('employeeapi/<int:pk>/', views.EmployeeRetrieve.as_view(),name='employee'),
    # path('employeeapi/<int:pk>/', views.EmployeeUpdate.as_view(),name='employee'),
    # path('employeeapi/<int:pk>/', views.EmployeeDestroy.as_view(),name='employee'),





]
