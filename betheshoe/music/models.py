from django.db import models
from betheshoe.movies.models import Movie

class Musician(models.Model):
    name = models.CharField(max_length=255, unique=True)
    hometown = models.CharField(max_length=255, blank=True, default="")
    movies = models.ManyToManyField(Movie, blank=True)
    image = models.ImageField(upload_to="musicians/", blank=True, null=True)
    order = models.IntegerField(default=0)
    publish = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    def get_movies(self):
        return self.movies.filter(publish=True).order_by('-year')


class Link(models.Model):

    ICONS = (
        ('myspace', "MySpace"),
        ('soundclound', "SoundCloud"),
        ('bandcamp', "BandCamp"),
        ('itunes', "iTunes"),
        ('amazon', "Amazon MP3"),
        ('twitter', "Twitter"),
        ('facebook', "Facebook"),
    )

    musician = models.ForeignKey(Musician)
    url = models.URLField()
    icon = models.CharField(max_length=255, choices=ICONS)

    def __unicode__(self):
        return "{}'s {}".format(self.musician, self.get_icon_display())