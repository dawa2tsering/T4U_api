from django.contrib import admin
from accounts.models import Account, AddTournament, Sponsor, Partner
# Register your models here.

admin.site.register([Account,AddTournament, Sponsor, Partner])
