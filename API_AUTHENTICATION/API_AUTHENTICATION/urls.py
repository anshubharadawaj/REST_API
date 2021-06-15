from django.contrib import admin
from django.urls import path, include
from Authentication_app import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
# from Authentication_app.views import CustomAuthToken

#creating  router object
router=DefaultRouter()

#register ViewSet with Router
# router.register('employeeapi',views.EmployeeViewSet, basename='employee')
router.register('employeeapi',views.EmployeeModelViewSet, basename='employee')
# router.register('employeeapi',views.EmployeeReadOnlyModelViewSet, basename='employee')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # for session authentication
    path('auth/',include('rest_framework.urls', namespace='rest_frameworrk')),

    #for fbv not used router
    # path('employee_api_fbv/',views.Employee_api),
    # path('employee_api_fbv/<int:pk>/',views.Employee_api),

    #for token aythentication
    # path('gettoken/',obtain_auth_token)

    # path('gettoken/',CustomAuthToken.as_view())
]

