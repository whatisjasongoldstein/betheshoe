# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_migrate_from_scruffyblog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='draft_ptr',
            field=models.AutoField(),
        ),
        migrations.RenameField(
            model_name='post',
            old_name='draft_ptr',
            new_name='id',
        ),
    ]
