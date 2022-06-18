from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


from rest_framework.authtoken.models import Token
# Create your models here.

#global variable for choices
USER_TYPE = (
		('Guest','Guest'),
		('Player','Player')
	)

#creating the model of user and extending the user model which includes varieties of attribute based on user model
class Account(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	user_type = models.CharField(max_length=100,choices=USER_TYPE)
	name = models.CharField(max_length=100)
	phone_no = models.PositiveIntegerField('Phone Number')
	photo = models.CharField(max_length=20000)
	level = models.CharField(max_length=100, null=True, blank=True)
	address = models.CharField(max_length=100, null=True, blank=True)
	zip_code = models.PositiveIntegerField(null=True, blank=True)
	created_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		# proxy = True
		# auto_created = True
		ordering = ('username',)
		verbose_name_plural = 'Accounts'

	def __str__(self):
		return "{} : {}".format(self.username, self.name)

	def check_username(self):
		try:
			if self.username == username:
				return Response('Username already exists')
		except:
			pass

	def check_user_type_images(self):
		try:
			if self.user_type == 'Player':
				return Response('You are permission to upload your images')
		except PermissionDenied:
			pass

		


#class tournament 
class Tournament(models.Model):
	banner_photo = models.CharField(max_length=20000)
	tournament_name = models.CharField(max_length=100, verbose_name='tournament_names', null=True, blank=True)
	start_date = models.DateField(auto_now_add=False)
	participation_deadline = models.DateField(auto_now_add=False)
	created_date = models.DateTimeField(auto_now_add=True)
	participation_fee = models.PositiveIntegerField()
	gym_name = models.CharField(max_length=100)
	street_address = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	zip_code = models.PositiveIntegerField()


	class Meta:
		verbose_name_plural = 'Tournaments'

	#using dunder method or magic method or special method
	def __str__(self):
		return "{}".format(self.tournament_name)



#class Team
class Team(models.Model):
	name = models.CharField(max_length=100)
	captain = models.CharField(max_length=100)
	score = models.PositiveIntegerField(default=0)
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True, blank=True, related_name='teams')



	class Meta:
		verbose_name_plural = 'Teams'

	def __str__(self):
		return "{}".format(self.name)

#class Match
class Match(models.Model):
	name = models.CharField(max_length=100)
	ground = models.CharField(max_length=100)
	start_date = models.DateTimeField(auto_now_add=False)
	team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1')
	team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2')
	score1 = models.PositiveIntegerField()
	score2 = models.PositiveIntegerField()
	date_created = models.DateTimeField(auto_now_add=True)
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='match')

	class Meta:
		verbose_name_plural='Matches'

	def __str__(self):
		return "{}".format(self.name)

		


#class playerparticipation
class PlayerParticipation(models.Model):
	# player_name = models.CharField(max_length=100, null=True, blank=True)
	# email = models.EmailField()
	# phone_no = models.PositiveIntegerField()
	# photo = models.CharField(max_length=20000)
	# level = models.CharField(max_length=100)
	# address = models.CharField(max_length=100)
	# zip_code = models.PositiveIntegerField()
	status = models.CharField(max_length=100)
	date_created = models.DateTimeField(auto_now_add=True)	
	players=models.ForeignKey(Account, on_delete=models.CASCADE, related_name='playerparticipations')
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='playerparticipations')


	class Meta:
		verbose_name_plural = 'PlayerParticipations'

	def __str__(self):
		return "{}".format(self.player_name)

#class teamplayer
class TeamPlayer(models.Model):
	team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name='teams')
	playerparticipation = models.ForeignKey(PlayerParticipation, on_delete=models.CASCADE, null=True, blank=True, related_name='teamplayerss')
	
	class Meta:
		verbose_name_plural = 'TeamPlayers'

	def __str__(self):
		return "{}".format(self.team)

#creating the class sponsor
class Sponsor(models.Model):
	name = models.CharField(max_length=100)
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='sponsors')
	photo = models.CharField(max_length=20000)

	class Meta:
		verbose_name_plural = 'Sponsors'

	def __str__(self):
		return "{}".format(self.name)


#creating the class partners
class Partner(models.Model):
	name = models.CharField(max_length=100)
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='partners')
	photo = models.CharField(max_length=20000)

	class Meta:
		verbose_name_plural = 'Partners'

	def __str__(self):
		return "{}".format(self.name)
