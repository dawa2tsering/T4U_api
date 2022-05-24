from django.shortcuts import render

from rest_framework import generics
from rest_framework import status

from api.serializers import RegisterSerializer

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
		return Response({'Errors':serializers.errors}, status=status.HTTP_400_BAD_REQUEST)
