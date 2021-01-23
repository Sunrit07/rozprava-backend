# Generated by Django 3.1.5 on 2021-01-23 19:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTPVerification',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('otp', models.CharField(max_length=6)),
                ('verifier_tag', models.IntegerField(choices=[(1, 'MAIL VERIFICATION'), (2, 'PHONE VERIFICATION'), (3, 'PASSWORD RESET'), (0, 'OTHER')])),
                ('is_verified', models.BooleanField(default=False)),
                ('notification_type', models.SmallIntegerField(choices=[(0, 'All'), (1, 'Sms'), (2, 'Email'), (3, 'Push'), (4, 'Call')], default=2)),
                ('additional_data', models.JSONField(blank=True, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
    ]
