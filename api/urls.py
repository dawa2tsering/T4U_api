from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import RegistrationAPIView

from .import views


#custom url
app_name = 'api'

urlpatterns = [
	path('api/register/', RegistrationAPIView.as_view(), name='auth-register'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/refresh-token/', TokenRefreshView.as_view(), name='refresh-token')
]