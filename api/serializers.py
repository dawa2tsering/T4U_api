
from rest_framework import serializers
from accounts.models import Account, Match, Sponsor, Partner, Tournament, PlayerParticipation, TeamPlayer,Team,Match

from django.contrib.auth.models import User


#register serializers for User using serializers
class RegisterSerializer(serializers.ModelSerializer):
	email = serializers.CharField(max_length=100)
	username = serializers.CharField(max_length=100)
	password = serializers.CharField(max_length=100, write_only=True)

	class Meta:
		model = User
		fields = ('id','username','email','password')

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


#sponsor Serializer
class SponsorSerializer(serializers.ModelSerializer):
	tournament = serializers.SlugRelatedField(queryset = Tournament.objects.all(),slug_field = 'id')
	class Meta:
		model = Sponsor
		fields = ['id','name','photo','tournament']
		depth = 1
		

#partner Serializer
class PartnerSerializer(serializers.ModelSerializer):
	tournament = serializers.SlugRelatedField(queryset = Tournament.objects.all(),slug_field = 'id')
	class Meta:
		model = Partner
		fields = ('id','name','photo','tournament')
		depth = 1
		

#playerparticipation serializer
class PlayerParticipationSerializer(serializers.ModelSerializer):
	tournament = serializers.SlugRelatedField(queryset = Tournament.objects.all(),slug_field = 'id')
	players = serializers.SlugRelatedField(queryset = Account.objects.all(),slug_field = 'id')

	class Meta:
		model = PlayerParticipation
		fields = ['id','status','date_created','players','tournament',]
		# fields = ['id','player_name','email','phone_no','photo','level','address','zip_code','status','tournament','date_created']
		depth = 1


#tournament serializer
class TeamSerializer(serializers.ModelSerializer):
	tournament = serializers.SlugRelatedField(queryset = Tournament.objects.all(),slug_field = 'id')
	class Meta:
		model = Team
		fields = ['id','name','captain','score','tournament']
		depth = 1


class MatchSerializer(serializers.ModelSerializer):

	#to insert foreign key
	tournament = serializers.SlugRelatedField(queryset = Tournament.objects.all(),slug_field = 'id')
	team1 = serializers.SlugRelatedField(queryset = Team.objects.all(),slug_field = 'id')
	team2 = serializers.SlugRelatedField(queryset = Team.objects.all(),slug_field = 'id')

	class Meta:
		model = Match
		fields = ['id','name','ground','start_date','team1','team2','score1','score2','date_created','tournament']
		depth = 1


#tournamentserializer
class TournamentSerializer(serializers.ModelSerializer):
	#nested serializers
	sponsors = SponsorSerializer(many=True, read_only=True)
	partners = PartnerSerializer(many=True, read_only=True)
	playerparticipations = PlayerParticipationSerializer(many=True, read_only=True)
	teams = TeamSerializer(many=True, read_only=True)
	match = MatchSerializer(many=True, read_only=True)

	#we need to add team serailizer in this  seralizers
	class Meta:
		model = Tournament
		fields = ['id','banner_photo','tournament_name','start_date','participation_deadline','created_date','participation_fee',
				'gym_name','street_address','city','state','zip_code','sponsors','partners','playerparticipations','teams','match']
		depth = 1

#tournamelistserializer
class TournamentListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tournament
		fields = ['id','banner_photo','tournament_name','start_date','created_date','gym_name','street_address','city','state','zip_code',]
		
		depth = 1


#teamplayer seralizers
class TeamPlayerSerializer(serializers.ModelSerializer):
	# teamplayers = TeamSerializer(many=True, read_only=True)
	# teamplayerss = PlayerParticipationSerializer(many=True, read_only=True)
	class Meta:
		model = TeamPlayer
		fields = ['team','playerparticipation']
		depth = 1



