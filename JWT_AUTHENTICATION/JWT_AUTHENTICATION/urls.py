from django.contrib import admin
from django.urls import path, include
from JWT_Auth_app import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


#creating  router object
router=DefaultRouter()

#register ViewSet with Router
# router.register('employeeapi',views.EmployeeViewSet, basename='employee')
router.register('employeeapi',views.EmployeeModelViewSet, basename='employee')
# router.register('employeeapi',views.EmployeeReadOnlyModelViewSet, basename='employee')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='refresh_token'),
    path('verifytoken/',TokenVerifyView.as_view(), name='verify_token'),

]

