# Generated by Django 3.2.6 on 2022-06-18 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('Guest', 'Guest'), ('Player', 'Player')], max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('phone_no', models.PositiveIntegerField(verbose_name='Phone Number')),
                ('photo', models.CharField(max_length=20000)),
                ('level', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('zip_code', models.PositiveIntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Accounts',
                'ordering': ('username',),
            },
        ),
        migrations.CreateModel(
            name='PlayerParticipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('players', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playerparticipations', to='accounts.account')),
            ],
            options={
                'verbose_name_plural': 'PlayerParticipations',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('captain', models.CharField(max_length=100)),
                ('score', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_photo', models.CharField(max_length=20000)),
                ('tournament_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='tournament_names')),
                ('start_date', models.DateField()),
                ('participation_deadline', models.DateField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('participation_fee', models.PositiveIntegerField()),
                ('gym_name', models.CharField(max_length=100)),
                ('street_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Tournaments',
            },
        ),
        migrations.CreateModel(
            name='TeamPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerparticipation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teamplayerss', to='accounts.playerparticipation')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='accounts.team')),
            ],
            options={
                'verbose_name_plural': 'TeamPlayers',
            },
        ),
        migrations.AddField(
            model_name='team',
            name='tournament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='accounts.tournament'),
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=20000)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsors', to='accounts.tournament')),
            ],
            options={
                'verbose_name_plural': 'Sponsors',
            },
        ),
        migrations.AddField(
            model_name='playerparticipation',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playerparticipations', to='accounts.tournament'),
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=20000)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partners', to='accounts.tournament')),
            ],
            options={
                'verbose_name_plural': 'Partners',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ground', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('score1', models.PositiveIntegerField()),
                ('score2', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='accounts.team')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='accounts.team')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='accounts.tournament')),
            ],
            options={
                'verbose_name_plural': 'Matches',
            },
        ),
    ]
