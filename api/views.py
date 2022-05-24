from django.shortcuts import render
from django.shortcuts import render

from rest_framework import generics
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import serializers

from accounts.models import Account

from api.serializers import RegisterSerializer, UserModelSerializer

import uuid
# Create your views here.

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



class UserModelListCreate(generics.ListCreateAPIView):
	serializer_class = UserModelSerializer
	queryset = Account.objects.all()


class UserModelRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = UserModelSerializer
	queryset = Account.objects.all()
	lookup_field = 'id'