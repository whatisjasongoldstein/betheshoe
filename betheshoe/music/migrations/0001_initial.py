# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('icon', models.CharField(max_length=255, choices=[(b'myspace', b'MySpace'), (b'soundclound', b'SoundCloud'), (b'bandcamp', b'BandCamp'), (b'itunes', b'iTunes'), (b'amazon', b'Amazon MP3'), (b'twitter', b'Twitter'), (b'facebook', b'Facebook')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('hometown', models.CharField(default=b'', max_length=255, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'musicians/', blank=True)),
                ('order', models.IntegerField(default=0)),
                ('publish', models.BooleanField(default=True)),
                ('movies', models.ManyToManyField(to='movies.Movie', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='link',
            name='musician',
            field=models.ForeignKey(to='music.Musician'),
            preserve_default=True,
        ),
    ]
