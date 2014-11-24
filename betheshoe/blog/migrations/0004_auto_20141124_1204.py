# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def sync_with_drafts(apps, schema_editor):
    Post = apps.get_model("blog", "post")
    for post in Post.objects.all():
        post.draft_id = post.id
        post.save()

class Migration(migrations.Migration):

    dependencies = [
        ('draftin', '0004_draft_date_published'),
        ('blog', '0003_auto_20141124_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.OneToOneField(default=None, null=True, to='draftin.Draft'),
            preserve_default=False,
        ),
        migrations.RunPython(sync_with_drafts),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
    ]
