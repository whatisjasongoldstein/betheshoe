# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(0, 'Nominated'), (1, 'Winner')])),
                ('movie', models.ForeignKey(to='movies.Movie', to_field=u'id')),
                ('event', models.ForeignKey(to_field=u'id', blank=True, to='movies.Show', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
