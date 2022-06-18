from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login


from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from accounts.models import Account, Sponsor, Partner, Tournament, PlayerParticipation, Team, TeamPlayer, Match

from knox.auth import AuthToken

from api.serializers import (AccountModelSerializer,UserSerializer,SponsorSerializer, PartnerSerializer,
							TournamentSerializer,TournamentListSerializer,PlayerParticipationSerializer, TeamSerializer, 
							TeamPlayerSerializer,MatchSerializer, RegisterSerializer, LoginUserSerializer)

from knox.views import LoginView as KnoxLoginView

# Create your views here.
class RegisterAPI(generics.GenericAPIView):
	serializer_class = RegisterSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		return Response({
			'user':UserSerializer(user, context=self.get_serializer_context()).data,
			'token':AuthToken.objects.create(user)[1]
		})

#login api 
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


#user api
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

#paginations in api
class CustomPagination(PageNumberPagination):
	page_size = 10
	page_size_query_param = 'page_size'
	max_page_size = 1000

	def get_paginated_response(self, data):
		return Response({
				'links':{
					'next':self.get_next_link(),
					'previous':self.get_previous_link(),
				},
				'count':self.page.paginator.count,
				'page_size':self.page_size,
				'results':data
			})

#list create api for UserModel
class UserModelListCreate(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = AccountModelSerializer
	queryset = Account.objects.all()



#to delete,update, retrieve update for user model
class UserModelRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = AccountModelSerializer
	queryset = Account.objects.all()
	lookup_field = 'id'



#sponsor crud in api
class SponsorListCreate(generics.ListCreateAPIView): 
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = SponsorSerializer
	queryset = Sponsor.objects.all()
	#pagination_class = CustomPagination

class SponsorRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = SponsorSerializer
	queryset = Sponsor.objects.all()
	lookup_field = 'id'


#partner crud in api

class PartnerListCreate(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = PartnerSerializer
	queryset = Partner.objects.all()
	#pagination_class = CustomPagination

class PartnerRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = PartnerSerializer
	queryset = Partner.objects.all()
	lookup_field = 'id'


#add-tournament crud api url
class TournamentListCreate(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = TournamentSerializer
	queryset = Tournament.objects.all()
	pagination_class = CustomPagination



class GetTournamentList(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = TournamentListSerializer
	queryset = Tournament.objects.all()
	pagination_class = CustomPagination


class TournamentUpdateRetreiveDestroy(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = TournamentSerializer
	queryset = Tournament.objects.all()
	lookup_field = 'id'


#playerparticipation crudapi url
class PlayerParticipationListCreate(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = PlayerParticipationSerializer
	queryset = PlayerParticipation.objects.all()
	pagination_class = CustomPagination

class PlayerParticipationUpdateRetreiveDestroy(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = PlayerParticipationSerializer
	queryset = PlayerParticipation.objects.all()
	lookup_field = 'id'


#Team serializer
class TeamListCreate(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = TeamSerializer
	queryset = Team.objects.all()


class TeamUpdateRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = TeamSerializer
	queryset = Team.objects.all()
	lookup_field = 'id'


class TeamPlayerListCreate(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = TeamPlayerSerializer
	queryset = TeamPlayer.objects.all()

class TeamPlayerRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = TeamPlayerSerializer
	querysett = TeamPlayer.objects.all()
	lookup_field = 'id'


class MatchListCreate(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = MatchSerializer
	queryset = Match.objects.all()

class MatchRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = MatchSerializer
	queryset = Match.objects.all()
	lookup_field ='id'

