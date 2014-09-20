# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('icon', models.CharField(max_length=255, choices=[(b'website', b'Website'), (b'blog', b'Blog'), (b'imdb', b'IMDB'), (b'portfolio', b'Portfolio'), (b'twitter', b'Twitter'), (b'Flickr', b'Flickr'), (b'youtube', b'YouTube'), (b'email', b'Email'), (b'linkedin', b'LinkedIn'), (b'facebook', b'Facebook')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staffer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('image', models.ImageField(default=b'', upload_to=b'staff/', blank=True)),
                ('bio', models.TextField(default=b'', blank=True)),
                ('publish', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
                ('group', models.ForeignKey(to='staff.Group', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='socialprofile',
            name='staffer',
            field=models.ForeignKey(to='staff.Staffer'),
            preserve_default=True,
        ),
    ]
