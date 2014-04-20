# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialProfile',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('staffer', models.ForeignKey(to='staff.Staffer', to_field=u'id')),
                ('url', models.URLField()),
                ('icon', models.CharField(max_length=255, choices=[('website', 'Website'), ('blog', 'Blog'), ('imdb', 'IMDB'), ('portfolio', 'Portfolio'), ('twitter', 'Twitter'), ('Flickr', 'Flickr'), ('youtube', 'YouTube'), ('email', 'Email'), ('linkedin', 'LinkedIn'), ('facebook', 'Facebook')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
