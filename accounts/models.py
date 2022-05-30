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
class Account(User):
	#username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	#password = models.CharField(max_length=100)
	user_type = models.CharField(max_length=100, choices=USER_TYPE)
	name = models.CharField(max_length=100)
	#email = models.EmailField()
	phone_no = models.PositiveIntegerField('Phone Number')
	photo = models.ImageField(upload_to='player/image', null=True, blank=True)
	level = models.CharField(max_length=100, null=True, blank=True)
	address = models.CharField(max_length=100, null=True, blank=True)
	zip_code = models.PositiveIntegerField(null=True, blank=True)
	created_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('username',)
		verbose_name_plural = 'Accounts'

	def __str__(self):
		return "{} : {}".format(self.username, self.name)


#class tournament 
class Tournament(models.Model):
	banner_photo = models.ImageField(upload_to='banner/photo')
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




#creating the class sponsor
class Sponsor(models.Model):
	name = models.CharField(max_length=100)
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='sponsors')
	photo = models.ImageField(upload_to='sponsors/photo')

	class Meta:
		verbose_name_plural = 'Sponsors'

	def __str__(self):
		return "{}".format(self.name)


#creating the class sponsor
class Partner(models.Model):
	name = models.CharField(max_length=100)
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='partners')
	photo = models.ImageField(upload_to='partners/photo')

	class Meta:
		verbose_name_plural = 'Partners'

	def __str__(self):
		return "{}".format(self.name)


#creating the class playerparticipation
class PlayerParticipation(models.Model):
	player_name = models.CharField(max_length=100, null=True, blank=True)
	email = models.EmailField()
	phone_no = models.PositiveIntegerField()
	photo = models.ImageField(upload_to='playerparticipation/photo')
	level = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	zip_code = models.PositiveIntegerField()
	status = models.CharField(max_length=100)
	date_created = models.DateTimeField(auto_now_add=True)	
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='playerparticipations')


	class Meta:
		verbose_name_plural = 'PlayerParticipations'

	def __str__(self):
		return "{}".format(self.player_name)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)