# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(0, b'Nominated'), (1, b'Winner')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('year', models.IntegerField(max_length=4)),
                ('length', models.IntegerField(default=0, help_text=b'In minutes', blank=True)),
                ('synopsis', models.TextField(default=b'', blank=True)),
                ('image', models.ImageField(default=b'', upload_to=b'movies/', blank=True)),
                ('poster', models.ImageField(default=b'', upload_to=b'poster/', blank=True)),
                ('trailer_url', models.URLField(default=b'', blank=True)),
                ('full_url', models.URLField(default=b'', blank=True)),
                ('publish', models.BooleanField(default=True)),
                ('imdb', models.URLField(default=b'', blank=True)),
                ('genre', models.CharField(default=b'', max_length=255, blank=True, choices=[(b'action', b'Action'), (b'adventure', b'Adventure'), (b'comedy', b'Comedy'), (b'crime', b'Crime'), (b'documentary', b'Documentary'), (b'drama', b'Drama'), (b'family', b'Family'), (b'fantasy', b'Fantasy'), (b'film-noir', b'Film-Noir'), (b'history', b'History'), (b'horror', b'Horror'), (b'music-video', b'Music Video'), (b'musical', b'Musical'), (b'mystery', b'Mystery'), (b'news', b'News'), (b'romance', b'Romance'), (b'romantic-comedy', b'Romantic Comedy'), (b'science Fiction', b'Science Fiction'), (b'thriller', b'Thriller'), (b'western', b'Western')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=255)),
                ('date', models.DateField(null=True, blank=True)),
                ('time', models.TimeField(null=True, blank=True)),
                ('slug', models.SlugField()),
                ('summary', models.TextField(null=True, verbose_name=b'Description', blank=True)),
                ('event_type', models.CharField(max_length=255, verbose_name=b'Type', choices=[(b'premiere', b'Premiere'), (b'festival', b'Film Festival'), (b'show', b'Screening')])),
                ('city', models.CharField(default=b'', max_length=255)),
                ('state', models.CharField(default=b'', max_length=2)),
                ('venue', models.CharField(default=b'', max_length=255)),
                ('venue_link', models.URLField(default=b'', blank=True)),
                ('facebook_event', models.URLField(default=b'', blank=True)),
                ('movie', models.ForeignKey(to='movies.Movie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='award',
            name='event',
            field=models.ForeignKey(related_name=b'awards', blank=True, to='movies.Show', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='award',
            name='movie',
            field=models.ForeignKey(to='movies.Movie'),
            preserve_default=True,
        ),
    ]
