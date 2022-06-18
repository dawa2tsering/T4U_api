from rest_framework import serializers, validators
from accounts.models import Account, Match, Sponsor, Partner, Tournament, PlayerParticipation, TeamPlayer,Team,Match,Team1,Team2

from django.contrib.auth.models import User
from django.contrib.auth import authenticate


#Register Serializer
#register serializers for User using serializers
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username','email')


#Register Serializers
class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username','email','password')
		extra_kwargs = {'password':{'write_only':True}}

	def create(self, validate_data):
		user = User.objects.create_user(validate_data['username'], validate_data['email'], validate_data['password'])
		return user


#login serailizer
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")




#usermodel Serializer
class AccountModelSerializer(serializers.ModelSerializer):
	username = serializers.SlugRelatedField(queryset = User.objects.all(),slug_field = 'id')
	class Meta:
		model = Account
		fields = ['id','username','user_type','name','phone_no','photo','level','address','zip_code','created_date']
		depth = 1


class SponsorSerializer(serializers.ModelSerializer):
	tournament = serializers.SlugRelatedField(queryset = Tournament.objects.all(),slug_field = 'id')
	class Meta:
		model = Sponsor
		fields = ['id','name','status','photo','tournament']
		depth = 1
		

#partner Serializer
class PartnerSerializer(serializers.ModelSerializer):
	tournament = serializers.SlugRelatedField(queryset = Tournament.objects.all(),slug_field = 'id')
	class Meta:
		model = Partner
		fields = ('id','name','status','photo','tournament')
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

class TeamPlayerSerializer(serializers.ModelSerializer):
	team = serializers.SlugRelatedField(queryset = Team.objects.all(),slug_field = 'id')
	playerparticipation = serializers.SlugRelatedField(queryset = PlayerParticipation.objects.all(),slug_field = 'id')
	tournament = serializers.SlugRelatedField(queryset = Tournament.objects.all(),slug_field = 'id')
	class Meta:
		model = TeamPlayer
		fields = ['id','team','playerparticipation','tournament']
		depth = 1


class TeamSerializer(serializers.ModelSerializer):
	tournament = serializers.SlugRelatedField(queryset = Tournament.objects.all(),slug_field = 'id')
	captain = serializers.SlugRelatedField(queryset = PlayerParticipation.objects.all(),slug_field = 'id')
	teamplayer= TeamPlayerSerializer(many=True, read_only=True)
	class Meta:
		model = Team
		fields = ['id','name','captain','score','tournament','teamplayer']
		depth = 1

class TeamListSerializer(serializers.ModelSerializer):
	tournament = serializers.SlugRelatedField(queryset = Tournament.objects.all(),slug_field = 'id')
	captain = serializers.SlugRelatedField(queryset = PlayerParticipation.objects.all(),slug_field = 'id')
	teamplayer= TeamPlayerSerializer(many=True, read_only=True)
	class Meta:
		model = Team
		fields = ['id','name','captain','score','tournament','teamplayer']
		depth = 1



#team seralizers

#teamplayer seralizers

class Team1Serializer(serializers.ModelSerializer):
	tournament = serializers.SlugRelatedField(queryset = Tournament.objects.all(),slug_field = 'id')
	match = serializers.SlugRelatedField(queryset = Match.objects.all(),slug_field = 'id')
	team1 = serializers.SlugRelatedField(queryset = Team.objects.all(),slug_field = 'id')
	player1 = serializers.SlugRelatedField(queryset = TeamPlayer.objects.all(),slug_field = 'id')
	player2 = serializers.SlugRelatedField(queryset = TeamPlayer.objects.all(),slug_field = 'id')

	class Meta:
		model = Team1
		fields = ['id','tournament','match','team1','player1','player2']
		depth = 1

class Team2Serializer(serializers.ModelSerializer):
	tournament = serializers.SlugRelatedField(queryset = Tournament.objects.all(),slug_field = 'id')
	match = serializers.SlugRelatedField(queryset = Match.objects.all(),slug_field = 'id')
	team2 = serializers.SlugRelatedField(queryset = Team.objects.all(),slug_field = 'id')
	player1 = serializers.SlugRelatedField(queryset = TeamPlayer.objects.all(),slug_field = 'id')
	player2 = serializers.SlugRelatedField(queryset = TeamPlayer.objects.all(),slug_field = 'id')

	class Meta:
		model = Team2
		fields = ['id','tournament','match','team2','player1','player2']
		depth = 1

class MatchSerializer(serializers.ModelSerializer):
	tournament = serializers.SlugRelatedField(queryset = Tournament.objects.all(),slug_field = 'id')
	team1 = serializers.SlugRelatedField(queryset = Team.objects.all(),slug_field = 'id')
	team2 = serializers.SlugRelatedField(queryset = Team.objects.all(),slug_field = 'id')
	team1_player=Team1Serializer(many=True, read_only=True)
	team2_player=Team1Serializer(many=True, read_only=True)

	class Meta:
		model = Match
		fields = ['id','name','ground','start_date','team1','team2','team1_player','team2_player','score1','score2','date_created','tournament']
		depth = 1



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


class TournamentListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tournament
		fields = ['id','banner_photo','tournament_name','start_date','created_date','gym_name','street_address','city','state','zip_code',]
		
		depth = 1