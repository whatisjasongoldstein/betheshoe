# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='movies',
            field=models.ManyToManyField(to='movies.Movie', blank=True),
        ),
    ]
