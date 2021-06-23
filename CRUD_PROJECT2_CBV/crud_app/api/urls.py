from django.urls import path,include
from crud_app.api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('crud', views.UserViewset, basename='user')

urlpatterns=[
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='restframework'))

]