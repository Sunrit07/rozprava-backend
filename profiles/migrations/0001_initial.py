# Generated by Django 3.2.3 on 2021-05-23 02:29

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
                ('is_deleted', models.BooleanField(default=False)),
                ('dob', models.DateField(blank=True, null=True)),
                ('display_pic', models.ImageField(blank=True, null=True, upload_to='user/dp/')),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('celebrity_rank', models.SmallIntegerField(choices=[(0, 'Nobody'), (1, 'Micro Influencer'), (2, 'Influencer'), (3, 'Celebrity'), (4, 'Superstar'), (5, 'Admin')], default=0)),
                ('is_celebrity', models.BooleanField(default=False)),
                ('profession', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('TRANS', 'Transgender'), ('OTHER', 'Other')], max_length=10)),
                ('relationship_status', models.SmallIntegerField(choices=[(0, 'Single'), (1, 'Engaged'), (2, 'Married'), (3, 'Committed'), (4, 'Widowed')], default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InviteLead',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('is_deleted', models.BooleanField(default=False)),
                ('invited_type', models.SmallIntegerField(choices=[(0, 'Other'), (1, 'Mobile'), (2, 'Email')], default=0)),
                ('invited_contact', models.CharField(blank=True, max_length=120, null=True, unique=True)),
                ('has_registered', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
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
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('privacy', models.SmallIntegerField(choices=[(0, 'Public'), (1, 'Private')], default=0)),
                ('interview', models.JSONField(blank=True, null=True)),
                ('admins', models.ManyToManyField(related_name='admins', to='profiles.Profile')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='profiles.profile')),
                ('profile_requests', models.ManyToManyField(related_name='pending_request_profiles', to='profiles.Profile')),
                ('profiles', models.ManyToManyField(related_name='members', to='profiles.Profile')),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FollowerMap',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('is_deleted', models.BooleanField(default=False)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='profiles.profile')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='profiles.profile')),
            ],
            options={
                'unique_together': {('follower', 'following')},
            },
        ),
    ]
