from rest_framework import serializers
from accounts.models import Account, Sponsor, Partner, Tournament, PlayerParticipation, TeamPlayer,Team

from django.contrib.auth.models import User
from drf_extra_fields.fields import Base64ImageField


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
	photo = Base64ImageField()
	class Meta:
		model = Account
		fields = ['id','username','password','user_type','name','email','phone_no','photo','level','address','zip_code','created_date']
		depth = 1

	def create(self, validated_data):
		photo = validated_data.pop('photo')
		data = validated_data.pop('data')
		return Account.objects.create(data=data, photo=photo)
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


#tournament serializer
class TeamSerializer(serializers.ModelSerializer):
	#using nested serializers
	# teams = TournamentSerializer(many=True, read_only=True)
	class Meta:
		model = Team
		fields = ['name','captain','score','tournament']
		depth = 1

class TournamentSerializer(serializers.ModelSerializer):
	#nested serializers
	sponsors = SponsorSerializer(many=True, read_only=True)
	partners = PartnerSerializer(many=True, read_only=True)
	playerparticipations = PlayerParticipationSerializer(many=True, read_only=True)
	teams = TeamSerializer(many=True, read_only=True)

	#we need to add team serailizer in this  seralizerss
	class Meta:
		model = Tournament
		fields = ['id','banner_photo','tournament_name','start_date','participation_deadline','created_date','participation_fee',
				'gym_name','street_address','city','state','zip_code','sponsors','partners','playerparticipations','teams']
		
		depth = 1

#team seralizers

#teamplayer seralizers
class TeamPlayerSerializer(serializers.ModelSerializer):
	# teamplayers = TeamSerializer(many=True, read_only=True)
	# teamplayerss = PlayerParticipationSerializer(many=True, read_only=True)
	class Meta:
		model = TeamPlayer
		fields = ['team','playerparticipation']
		depth = 1

