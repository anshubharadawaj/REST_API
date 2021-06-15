
from django.contrib import admin
from django.urls import path, include
from viewset_app import views
from rest_framework.routers import DefaultRouter

#creating  router object
router=DefaultRouter()

#register ViewSet with Router
# router.register('employeeapi',views.EmployeeViewSet, basename='employee')
# router.register('employeeapi',views.EmployeeModelViewSet, basename='employee')
router.register('employeeapi',views.EmployeeReadOnlyModelViewSet, basename='employee')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
