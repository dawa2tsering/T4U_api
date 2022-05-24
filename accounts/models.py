from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#global variable for choices
USER_TYPE = (
		('Guest','Guest'),
		('Player','Player')
	)

class UserModel(models.Model):
	username = models.OneToOneField(User, on_delete=models.CASCADE)
	password = models.CharField(max_length=100)
	user_type = models.CharField(max_length=100, choices=USER_TYPE)
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone_no = models.PositiveIntegerField('Phone Number')
	photo = models.ImageField(upload_to='player/image', null=True, blank=True)
	level = models.CharField(max_length=100, null=True, blank=True)
	address = models.CharField(max_length=100, null=True, blank=True)
	zip_code = models.PositiveIntegerField(null=True, blank=True)
	created_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('username',)
		verbose_name_plural = 'Guests'

	def __str__(self):
		return "{} : {}".format(self.username, self.name)
