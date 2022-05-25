from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import (RegistrationAPIView,UserModelListCreate, UserModelRetreiveUpdateDestroy, 
                    SponsorListCreate,SponsorRetreiveUpdateDestroy, PartnerListCreate,PartnerRetreiveUpdateDestroy,
                    AddTournamentListCreate,AddTournamentUpdateRetreiveDestroy)
from api.serializers import UserModelSerializer

from .import views


#custom url
app_name = 'api'


#url for api
urlpatterns = [
	path('api/register/', RegistrationAPIView.as_view(), name='auth-register'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),

    path('api/register/usermodel/',UserModelListCreate.as_view(), name='register-usermodel'),
    path('api/list/usermodel/<int:id>/', UserModelRetreiveUpdateDestroy.as_view(), name='list-usermodel'),


    #add-tournament api url
    path('api/listcreate/addtournament/',AddTournamentListCreate.as_view(),name='tournament-create'),
    path('api/update/tournament/<int:id>/',AddTournamentUpdateRetreiveDestroy.as_view(), name='tournament-update'),

    #sponsor api url
    path('api/listcreate/sponsor/',SponsorListCreate.as_view(), name='sponsors-create'),
    path('api/update/sponsor/<int:id>/', SponsorRetreiveUpdateDestroy.as_view(), name='sponsors-update'),


    #partner api url
    path('api/listcreate/partner/', PartnerListCreate.as_view(), name='partners-create'),
    path('api/update/partner/<int:id>/', PartnerRetreiveUpdateDestroy.as_view(), name='partners-update')


]