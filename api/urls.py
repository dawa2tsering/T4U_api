from django.urls import path


from api.views import (UserModelListCreate, UserModelRetreiveUpdateDestroy, 
                    SponsorListCreate,SponsorRetreiveUpdateDestroy, PartnerListCreate,PartnerRetreiveUpdateDestroy,
                    TournamentListCreate,GetTournamentList,TournamentUpdateRetreiveDestroy,PlayerParticipationListCreate,
                    PlayerParticipationUpdateRetreiveDestroy,TeamListCreate,TeamUpdateRetreiveUpdateDestroy,
                    TeamPlayerListCreate,TeamPlayerRetreiveUpdateDestroy,MatchListCreate,MatchRetrieveUpdateDestroy,
                    RegisterAPI, LoginAPI, UserAPI,Team1ListCreate,Team1RetrieveUpdateDestroy,Team2ListCreate,Team2RetrieveUpdateDestroy,TeamListUpdateRetreiveUpdateDestroy,TeamCreate)

from api.serializers import AccountModelSerializer

from knox import views as knox_views


from .import views


#custom url
app_name = 'api'


#url for api
urlpatterns = [

    #register api
    path('api/register/', RegisterAPI.as_view(), name='register-api'),

    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/user/', UserAPI.as_view(), name='user'),

    #add and get registered user
    path('api/register/accountmodel/',UserModelListCreate.as_view(), name='register-usermodel'),
    #crud registered user by id
    path('api/list/accountmodel/<int:id>/', UserModelRetreiveUpdateDestroy.as_view(), name='list-usermodel'),


    #add and get tournament api url for tournament detail
    path('api/listcreate/tournament/',TournamentListCreate.as_view(),name='tournament-create'),
    #get-tournament list api url for tournament view
    path('api/tournament/list',GetTournamentList.as_view(),name='tournament-get'),
    #crud tournament by id
    path('api/update/tournament/<int:id>/',TournamentUpdateRetreiveDestroy.as_view(), name='tournament-update'),

    #add and get sponsor api url
    path('api/listcreate/sponsor/',SponsorListCreate.as_view(), name='sponsors-create'),
    #crud sponsor by id
    path('api/update/sponsor/<int:id>/', SponsorRetreiveUpdateDestroy.as_view(), name='sponsors-update'),


    #add and get partner api url
    path('api/listcreate/partner/', PartnerListCreate.as_view(), name='partners-create'),
    #crud partner by id
    path('api/update/partner/<int:id>/', PartnerRetreiveUpdateDestroy.as_view(), name='partners-update'),

    #add and get playerparticipation api url
    path('api/listcreate/playerparticipation/',PlayerParticipationListCreate.as_view(), name='playerparticipation-create'),
    #crud playerparticipation by id
    path('api/update/playerparticipation/<int:id>/', PlayerParticipationUpdateRetreiveDestroy.as_view(), name='playerparticipation-update'),


    #add and get team api url
    path('api/team/create/', TeamCreate.as_view(), name='team-create'),
    #crud team by id
    path('api/team/update/<int:id>/', TeamUpdateRetreiveUpdateDestroy.as_view(), name='team-update'),

    #add and get team api url
    path('api/teamlist/create/', TeamListCreate.as_view(), name='teamlist-create'),
    #crud team by id
    path('api/teamlist/update/<int:id>/', TeamListUpdateRetreiveUpdateDestroy.as_view(), name='teamlist-update'),


    path('api/match/create/',MatchListCreate.as_view(), name='match-create'),
    path('api/match/update/<int:id>/', MatchRetrieveUpdateDestroy.as_view(), name='match-update'),

    #add and get teamplayer api url
    path('api/teamplayer/create/', TeamPlayerListCreate.as_view(), name='teamplayer-create'),
    #crud teamplayer by id
    path('api/teamplayer/update/<int:id>/', TeamPlayerRetreiveUpdateDestroy.as_view(), name='teamplayer-update'),

    #add and get team1 api url
    path('api/team1/create/', Team1ListCreate.as_view(), name='team1-create'),
    #crud team1 by id
    path('api/team1/update/<int:id>/', Team1RetrieveUpdateDestroy.as_view(), name='team1-update'),

    #add and get team1 api url
    path('api/team2/create/', Team2ListCreate.as_view(), name='team2-create'),
    #crud team1 by id
    path('api/team2/update/<int:id>/', Team2RetrieveUpdateDestroy.as_view(), name='team2-update'),
]