# Generated by Django 3.2.3 on 2021-05-23 02:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tracker', '0001_initial'),
        ('profiles', '0001_initial'),
        ('activity', '0001_initial'),
        ('case', '0001_initial'),
        ('proof', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debate',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_posted_anonymously', models.BooleanField(default=False)),
                ('comment', models.TextField()),
                ('inclination', models.SmallIntegerField(choices=[(1, 'For'), (0, 'Against')], default=1)),
                ('status', models.SmallIntegerField(choices=[(0, 'Revoked'), (1, 'Active'), (2, 'Under Review')], default=1)),
                ('votes_to_shift_to_for', models.IntegerField(default=0)),
                ('votes_to_shift_to_against', models.IntegerField(default=0)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case.case')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.location')),
                ('pointer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='debate.debate')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
                ('proofs', models.ManyToManyField(to='proof.Proof')),
                ('tags', models.ManyToManyField(to='activity.HashTag')),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DebateImpactHit',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('is_deleted', models.BooleanField(default=False)),
                ('impact', models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('debate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='debate.debate')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
            options={
                'unique_together': {('profile', 'debate')},
            },
        ),
    ]
