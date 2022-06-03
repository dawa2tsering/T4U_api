from django.contrib import admin
from accounts.models import Account, Tournament, Sponsor, Partner, PlayerParticipation, Team, TeamPlayer
# Register your models here.

admin.site.register([Account,Tournament, Sponsor, Partner,PlayerParticipation,Team,TeamPlayer])
