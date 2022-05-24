from rest_framework import serializers
from accounts.models import Account

from django.contrib.auth.models import User


#register serializers for User
class RegisterSerializer(serializers.ModelSerializer):
	email = serializers.CharField(max_length=100)
	username = serializers.CharField(max_length=100)
	password = serializers.CharField(max_length=100, write_only=True)

	class Meta:
		model = User
		fields = ('username','email','password')

	def validate(self, args):
		email = args.get('email',None)
		username = args.get('username',None)

		#making the condition whether the email is already exists for not
		if User.objects.filter(email = email).exists():
			raise serializers.ValidationError({'email':{'Email already exists'}})
		if User.objects.filter(username=username).exists():
			raise serializers.ValidationError({'username':{'Username already exists'}})

		return super().validate(args)


	#creating the user model directly by making create method
	def create(self, validated_data):
		return User.objects.create_user(**validated_data)


#usermodel Serializer
class UserModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ['id','username','password','user_type','name','email','phone_no','photo','level','address','zip_code','created_date']
		depth = 1

		#depth means how much the object will you want to fetch mostly commonly used is 1.It is basically used in nested serializers