# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('year', models.IntegerField(max_length=4)),
                ('length', models.IntegerField(default=0, help_text='In minutes', blank=True)),
                ('synopsis', models.TextField(default='', blank=True)),
                ('image', models.ImageField(default='', upload_to='movies/', blank=True)),
                ('poster', models.ImageField(default='', upload_to='poster/', blank=True)),
                ('trailer_url', models.URLField(default='', blank=True)),
                ('full_url', models.URLField(default='', blank=True)),
                ('publish', models.BooleanField(default=True)),
                ('imdb', models.URLField(default='', blank=True)),
                ('genre', models.CharField(default='', max_length=255, blank=True, choices=[('action', 'Action'), ('adventure', 'Adventure'), ('comedy', 'Comedy'), ('crime', 'Crime'), ('documentary', 'Documentary'), ('drama', 'Drama'), ('family', 'Family'), ('fantasy', 'Fantasy'), ('film-noir', 'Film-Noir'), ('history', 'History'), ('horror', 'Horror'), ('music-video', 'Music Video'), ('musical', 'Musical'), ('mystery', 'Mystery'), ('news', 'News'), ('romance', 'Romance'), ('romantic-comedy', 'Romantic Comedy'), ('science Fiction', 'Science Fiction'), ('thriller', 'Thriller'), ('western', 'Western')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default='', max_length=255)),
                ('date', models.DateField(null=True, blank=True)),
                ('time', models.TimeField(null=True, blank=True)),
                ('slug', models.SlugField()),
                ('summary', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('event_type', models.CharField(max_length=255, verbose_name='Type', choices=[('premiere', 'Premiere'), ('festival', 'Film Festival'), ('show', 'Screening')])),
                ('city', models.CharField(default='', max_length=255)),
                ('state', models.CharField(default='', max_length=2)),
                ('venue', models.CharField(default='', max_length=255)),
                ('venue_link', models.URLField(default='', blank=True)),
                ('facebook_event', models.URLField(default='', blank=True)),
                ('movie', models.ForeignKey(to='movies.Movie', to_field=u'id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
