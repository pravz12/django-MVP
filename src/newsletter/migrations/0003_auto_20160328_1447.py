 # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_signup_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='datestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 28, 14, 47, 49, 970802, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
