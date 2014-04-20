# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staffer',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('image', models.ImageField(default='', upload_to='staff/', blank=True)),
                ('bio', models.TextField(default='', blank=True)),
                ('publish', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
                ('group', models.ForeignKey(to='staff.Group', to_field=u'id', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
