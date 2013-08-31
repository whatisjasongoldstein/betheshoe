from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    year = models.IntegerField(max_length=4)
    length = models.IntegerField(default=0, blank=True, help_text="In minutes")
    synopsis = models.TextField(blank=True, default="")
    image = models.ImageField(upload_to="movies/", blank=True, default="")
    trailer_url = models.URLField(blank=True, default="")
    full_url = models.URLField(blank=True, default="")
    publish = models.BooleanField(default=True)
    imdb = models.URLField(blank=True, default="")

    def __unicode__(self):
        return self.title


class Show(models.Model):

    TYPES = (
        ('premiere', 'Premiere'),
        ('festival', 'Film Festival'),
        ('show', 'Show'),
    )

    title = models.CharField(max_length=255, default="")
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    slug = models.SlugField()
    summary = models.TextField(verbose_name="Description", blank=True, null=True)
    event_type = models.CharField(max_length=255, verbose_name="Type", choices=TYPES)
    city = models.CharField(max_length=255, default="")
    state = models.CharField(max_length=2, default="")
    venue = models.CharField(blank=False, max_length=255, default="")
    venue_link = models.URLField(blank=True, default="")
    facebook_event = models.URLField(blank=True, default="")

    movie = models.ForeignKey(Movie)

    def __unicode__(self):
        return "{} ({})".format(self.title, self.movie.title)


class Award(models.Model):
    LEVELS = (
        (0, "Nominated"),
        (1, "Winner"),
    )
    title = models.CharField(max_length=255)
    status = models.IntegerField(choices=LEVELS)
    movie = models.ForeignKey(Movie)
    event = models.ForeignKey(Show, blank=True, null=True)
