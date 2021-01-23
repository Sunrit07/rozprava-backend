# Generated by Django 3.1.5 on 2021-01-23 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('dob', models.DateField(blank=True, null=True)),
                ('display_pic', models.ImageField(blank=True, null=True, upload_to='user/dp/')),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('celebrity_rank', models.SmallIntegerField(choices=[(0, 'Nobody'), (1, 'Micro Influencer'), (2, 'Influencer'), (3, 'Celebrity'), (4, 'Superstar'), (5, 'Admin')], default=0)),
                ('profession', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('TRANS', 'Transgender')], max_length=10)),
                ('relationship_status', models.SmallIntegerField(choices=[(0, 'Single'), (1, 'Engaged'), (2, 'Married'), (3, 'Committed'), (4, 'Widowed')], default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('profiles', models.ManyToManyField(to='profiles.Profile')),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
    ]
