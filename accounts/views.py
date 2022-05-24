from django.shortcuts import render
from rest_framework import generics
# Create your views here.


class UserModelListCreate(generics.ListCreateAPIView):
	serializer_class = UserModelSerializer
	queryset = UserModel.objects.all()


class UserModelRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = UserModelSerializer
	queryset = UserModel.objects.all()
	lookup_field = 'id'