from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import RegistrationAPIView,UserModelListCreate, UserModelRetreiveUpdateDestroy
from api.serializers import UserModelSerializer

from .import views


#custom url
app_name = 'api'

urlpatterns = [
	path('api/register/', RegistrationAPIView.as_view(), name='auth-register'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),

    path('api/register/usermodel/',UserModelListCreate.as_view(), name='register-usermodel'),
    path('api/list/usermodel/<int:id>/', UserModelRetreiveUpdateDestroy.as_view(), name='list-usermodel')

]