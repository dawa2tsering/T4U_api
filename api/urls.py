from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import (RegistrationAPIView,UserModelListCreate, UserModelRetreiveUpdateDestroy, 
                    SponsorListCreate,SponsorRetreiveUpdateDestroy, PartnerListCreate,PartnerRetreiveUpdateDestroy,
                    TournamentListCreate,TournamentUpdateRetreiveDestroy,PlayerParticipationListCreate,
                    PlayerParticipationUpdateRetreiveDestroy,TeamListCreate,TeamUpdateRetreiveUpdateDestroy,
                    TeamPlayerListCreate,TeamPlayerRetreiveUpdateDestroy)
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
    path('api/listcreate/tournament/',TournamentListCreate.as_view(),name='tournament-create'),
    path('api/update/tournament/<int:id>/',TournamentUpdateRetreiveDestroy.as_view(), name='tournament-update'),

    #sponsor api url
    path('api/listcreate/sponsor/',SponsorListCreate.as_view(), name='sponsors-create'),
    path('api/update/sponsor/<int:id>/', SponsorRetreiveUpdateDestroy.as_view(), name='sponsors-update'),


    #partner api url
    path('api/listcreate/partner/', PartnerListCreate.as_view(), name='partners-create'),
    path('api/update/partner/<int:id>/', PartnerRetreiveUpdateDestroy.as_view(), name='partners-update'),

    #playerparticipation api url

    path('api/listcreate/playerparticipation/',PlayerParticipationListCreate.as_view(), name='playerparticipation-create'),
    path('api/update/playerparticipation/<int:id>/', PlayerParticipationUpdateRetreiveDestroy.as_view(), name='playerparticipation-update'),


    #team api url
    path('api/team/create/', TeamListCreate.as_view(), name='team-create'),
    path('api/team/update/<int:id>/', TeamUpdateRetreiveUpdateDestroy.as_view(), name='team-update'),

    #teamplayer api url
    path('api/teamplayer/create/', TeamPlayerListCreate.as_view(), name='teamplayer-create'),
    path('api/teamplayer/update/<int:id>/', TeamPlayerRetreiveUpdateDestroy.as_view(), name='teamplayer-update'),


]