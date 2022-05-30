from rest_framework import serializers
from accounts.models import Account, Sponsor, Partner, Tournament, PlayerParticipation

from django.contrib.auth.models import User


#register serializers for User using serializers
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

		#depth means how much the object will you want to fetch mostly commonly used is 1.


#sponsor Serializer
class SponsorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sponsor
		fields = ['id','name','photo','tournament']
		depth = 1
		

#partner Serializer
class PartnerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Partner
		fields = ['id','name','photo','tournament']
		depth = 1
		

#playerparticipation serializer
class PlayerParticipationSerializer(serializers.ModelSerializer):
	class Meta:
		model = PlayerParticipation
		fields = ['id','player_name','email','phone_no','photo','level','address','zip_code','status','tournament','date_created']
		depth = 1


#add-tournament serializer
class TournamentSerializer(serializers.ModelSerializer):
	#nested serializers
	sponsors = SponsorSerializer(many=True, read_only=True)
	partners = PartnerSerializer(many=True, read_only=True)
	playerparticipations = PlayerParticipationSerializer(many=True, read_only=True) 
	class Meta:
		model = Tournament
		fields = ['id','banner_photo','tournament_name','start_date','participation_deadline','created_date','participation_fee',
				'gym_name','street_address','city','state','zip_code','sponsors','partners','playerparticipations']
		
