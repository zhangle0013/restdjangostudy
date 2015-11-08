# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uEntryDate', models.DateTimeField(auto_created=True, blank=True)),
                ('uLogName', models.CharField(default=b'', max_length=50)),
                ('uPassword', models.CharField(default=b'', max_length=32)),
                ('uRealName', models.CharField(default=b'', max_length=50)),
                ('uAcronyName', models.CharField(default=b'', max_length=10)),
                ('uSpellName', models.CharField(default=b'', max_length=50)),
                ('uFirstName', models.CharField(default=b'', max_length=50)),
                ('uLastName', models.CharField(default=b'', max_length=50)),
                ('uIsDel', models.BooleanField(default=False)),
                ('uThumbnailSmall', models.ImageField(default=b'', upload_to=b'user', blank=True)),
                ('uThumbnail', models.ImageField(default=b'', upload_to=b'user', blank=True)),
                ('uIsFirst', models.BooleanField(default=True)),
                ('uEmail', models.EmailField(default=b'', max_length=254, blank=True)),
                ('uPhone', models.CharField(default=b'', max_length=50, blank=True)),
                ('uQQ', models.CharField(default=b'', max_length=50, blank=True)),
                ('uBirthday', models.DateTimeField(null=True, blank=True)),
                ('uLeaveDate', models.DateTimeField(null=True, blank=True)),
                ('uIdentity', models.CharField(default=b'', max_length=18, blank=True)),
                ('uGender', models.CharField(default=b'F', max_length=2, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('uDepartment', models.CharField(default=b'', max_length=50, blank=True)),
                ('uDuty', models.CharField(default=b'', max_length=50, blank=True)),
                ('uLevel', models.SmallIntegerField(null=True, blank=True)),
                ('uDutyStatus', models.SmallIntegerField(null=True, blank=True)),
                ('uWage', models.IntegerField(null=True, blank=True)),
                ('uRemark', models.TextField(default=b'', blank=True)),
            ],
        ),
    ]
