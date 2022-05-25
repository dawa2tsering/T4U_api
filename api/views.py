from django.shortcuts import render
from django.shortcuts import render

from rest_framework import generics
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import serializers

from accounts.models import Account, Sponsor, Partner, AddTournament

from api.serializers import RegisterSerializer, UserModelSerializer, SponsorSerializer, PartnerSerializer, AddTournamentSerializer

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



#list create api for UserModel
class UserModelListCreate(generics.ListCreateAPIView):
	serializer_class = UserModelSerializer
	queryset = Account.objects.all()



#to delete,update, retrieve update for user model
class UserModelRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = UserModelSerializer
	queryset = Account.objects.all()
	lookup_field = 'id'


#sponsor crud in api
class SponsorListCreate(generics.ListCreateAPIView):
	serializer_class = SponsorSerializer
	queryset = Sponsor.objects.all()

class SponsorRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = SponsorSerializer
	queryset = Sponsor.objects.all()
	lookup_field = 'id'


#partner crud in api

class PartnerListCreate(generics.ListCreateAPIView):
	serializer_class = PartnerSerializer
	queryset = Partner.objects.all()


class PartnerRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = PartnerSerializer
	queryset = Partner.objects.all()
	lookup_field = 'id'


#add-tournament crud api url
class AddTournamentListCreate(generics.ListCreateAPIView):
	serializer_class = AddTournamentSerializer
	queryset = AddTournament.objects.all()


class AddTournamentUpdateRetreiveDestroy(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = AddTournamentSerializer
	queryset = AddTournament.objects.all()
	lookup_field = 'id'