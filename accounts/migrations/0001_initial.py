# Generated by Django 3.2.6 on 2022-05-24 08:26

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
    ]
