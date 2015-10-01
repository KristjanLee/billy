# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='name',
            name='message',
        ),
        migrations.AddField(
            model_name='message',
            name='name_text',
            field=models.CharField(max_length=200, default=''),
        ),
        migrations.DeleteModel(
            name='Name',
        ),
    ]
