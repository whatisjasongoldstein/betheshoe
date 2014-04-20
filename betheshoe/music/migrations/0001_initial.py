# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_award'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('hometown', models.CharField(default='', max_length=255, blank=True)),
                ('image', models.ImageField(null=True, upload_to='musicians/', blank=True)),
                ('order', models.IntegerField(default=0)),
                ('publish', models.BooleanField(default=True)),
                ('movies', models.ManyToManyField(to='movies.Movie', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
