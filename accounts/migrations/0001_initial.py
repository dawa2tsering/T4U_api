# Generated by Django 3.2.6 on 2022-06-03 08:31

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('user_type', models.CharField(choices=[('Guest', 'Guest'), ('Player', 'Player')], max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('phone_no', models.PositiveIntegerField(verbose_name='Phone Number')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='player/image')),
                ('level', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('zip_code', models.PositiveIntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Accounts',
                'ordering': ('username',),
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PlayerParticipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.PositiveIntegerField()),
                ('photo', models.ImageField(upload_to='playerparticipation/photo')),
                ('level', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('zip_code', models.PositiveIntegerField()),
                ('status', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
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
                ('banner_photo', models.ImageField(upload_to='banner/photo')),
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
                ('playerparticipation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.playerparticipation')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teamplayers', to='accounts.team')),
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
                ('photo', models.ImageField(upload_to='sponsors/photo')),
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
                ('photo', models.ImageField(upload_to='partners/photo')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partners', to='accounts.tournament')),
            ],
            options={
                'verbose_name_plural': 'Partners',
            },
        ),
    ]
