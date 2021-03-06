# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(0, 'Nominated'), (1, 'Winner'), (2, 'Official Selection')])),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('year', models.IntegerField()),
                ('length', models.IntegerField(blank=True, default=0, help_text='In minutes')),
                ('synopsis', models.TextField(blank=True, default='')),
                ('image', models.ImageField(blank=True, default='', upload_to='movies/')),
                ('poster', models.ImageField(blank=True, default='', upload_to='poster/')),
                ('trailer_url', models.URLField(blank=True, default='')),
                ('full_url', models.URLField(blank=True, default='')),
                ('publish', models.BooleanField(default=True)),
                ('imdb', models.URLField(blank=True, default='')),
                ('genre', models.CharField(blank=True, choices=[('action', 'Action'), ('adventure', 'Adventure'), ('comedy', 'Comedy'), ('crime', 'Crime'), ('documentary', 'Documentary'), ('drama', 'Drama'), ('family', 'Family'), ('fantasy', 'Fantasy'), ('film-noir', 'Film-Noir'), ('history', 'History'), ('horror', 'Horror'), ('music-video', 'Music Video'), ('musical', 'Musical'), ('mystery', 'Mystery'), ('news', 'News'), ('romance', 'Romance'), ('romantic-comedy', 'Romantic Comedy'), ('science Fiction', 'Science Fiction'), ('thriller', 'Thriller'), ('western', 'Western')], default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('date', models.DateField(blank=True, null=True)),
                ('event_type', models.CharField(choices=[('premiere', 'Premiered'), ('festival', 'Film Festival'), ('show', 'Screened')], max_length=255, verbose_name='Type')),
                ('city', models.CharField(default='', max_length=255)),
                ('venue', models.CharField(default='', max_length=255)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='award',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='awards', to='movies.Show'),
        ),
        migrations.AddField(
            model_name='award',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
        ),
    ]
