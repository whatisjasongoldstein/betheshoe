# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('musician', models.ForeignKey(to='music.Musician', to_field=u'id')),
                ('url', models.URLField()),
                ('icon', models.CharField(max_length=255, choices=[('myspace', 'MySpace'), ('soundclound', 'SoundCloud'), ('bandcamp', 'BandCamp'), ('itunes', 'iTunes'), ('amazon', 'Amazon MP3'), ('twitter', 'Twitter'), ('facebook', 'Facebook')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
