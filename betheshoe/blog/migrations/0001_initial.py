# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
        ('draftin', '0003_auto_20141123_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('draft_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='draftin.Draft')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255, null=True, blank=True)),
                ('slug', models.SlugField(help_text=b'looks-like-this-and-should-never-change', unique=True, max_length=255)),
                ('image', models.ImageField(default=b'', help_text=b'Lead image. If this is not selected, the first visual in the body will be used.', upload_to=b'blog/%Y/%m', blank=True)),
                ('is_thumbnail', models.BooleanField(default=False, help_text=b"The image is only for thumbnails, don't use it as lead art.", verbose_name=b'Thumbnail only')),
                ('author', models.ForeignKey(blank=True, to='staff.Staffer', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
