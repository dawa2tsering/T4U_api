from django.shortcuts import render
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from rest_framework import generics
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from accounts.models import Account, Sponsor, Partner, Tournament, PlayerParticipation, Team, TeamPlayer

from api.serializers import (RegisterSerializer, UserModelSerializer, SponsorSerializer, PartnerSerializer,
							TournamentSerializer,PlayerParticipationSerializer, TeamSerializer, TeamPlayerSerializer)

import uuid
# Create your views here.

#registerthroughapi
class RegistrationAPIView(generics.GenericAPIView):
	serializer_class = RegisterSerializer

	def post(self, request):
		serializer = self.get_serializer(data=request.data)
		if(serializer.is_valid()):
			serializer.save()
			return Response({
					'RequestId':str(uuid.uuid4()),
					'Message':'User Created Successfully',
					'User':serializer.data
				}, status=status.HTTP_201_CREATED)
		return Response({'Errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



#paginations
class CustomPagination(PageNumberPagination):
	page_size = 1
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
	serializer_class = UserModelSerializer
	queryset = Account.objects.all()



#to delete,update, retrieve update for user model
class UserModelRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = UserModelSerializer
	queryset = Account.objects.all()
	lookup_field = 'id'

class PhotoList(APIView):
	def post(self, request, format=None):
		serializer = UserModelSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.photo.save()


#sponsor crud in api
class SponsorListCreate(generics.ListCreateAPIView):
	serializer_class = SponsorSerializer
	queryset = Sponsor.objects.all()
	pagination_class = CustomPagination

class SponsorRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = SponsorSerializer
	queryset = Sponsor.objects.all()
	lookup_field = 'id'


#partner crud in api

class PartnerListCreate(generics.ListCreateAPIView):
	serializer_class = PartnerSerializer
	queryset = Partner.objects.all()
	pagination_class = CustomPagination

class PartnerRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = PartnerSerializer
	queryset = Partner.objects.all()
	lookup_field = 'id'


#add-tournament crud api url
class TournamentListCreate(generics.ListCreateAPIView):
	serializer_class = TournamentSerializer
	queryset = Tournament.objects.all()
	pagination_class = CustomPagination


class TournamentUpdateRetreiveDestroy(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = TournamentSerializer
	queryset = Tournament.objects.all()
	lookup_field = 'id'


#playerparticipation crudapi url
class PlayerParticipationListCreate(generics.ListCreateAPIView):
	serializer_class = PlayerParticipationSerializer
	queryset = PlayerParticipation.objects.all()
	pagination_class = CustomPagination

class PlayerParticipationUpdateRetreiveDestroy(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = PlayerParticipationSerializer
	queryset = PlayerParticipation.objects.all()
	lookup_field = 'id'


#Team serializer
class TeamListCreate(generics.ListCreateAPIView):
	serializer_class = TeamSerializer
	queryset = Team.objects.all()


class TeamUpdateRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = TeamSerializer
	queryset = Team.objects.all()
	lookup_field = 'id'


class TeamPlayerListCreate(generics.ListCreateAPIView):
	serializer_class = TeamPlayerSerializer
	queryset = TeamPlayer.objects.all()

class TeamPlayerRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = TeamPlayerSerializer
	querysett = TeamPlayer.objects.all()
	lookup_field = 'id'