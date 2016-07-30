from django.db import models
from django.core.urlresolvers import reverse

from ..helpers import vimeo_embed_url

GENRES = (
    ("action", "Action"),
    ("adventure", "Adventure"),
    ("comedy", "Comedy"),
    ("crime", "Crime"),
    ("documentary", "Documentary"),
    ("drama", "Drama"),
    ("family", "Family"),
    ("fantasy", "Fantasy"),
    ("film-noir", "Film-Noir"),
    ("history", "History"),
    ("horror", "Horror"),
    ("music-video", "Music Video"),
    ("musical", "Musical"),
    ("mystery", "Mystery"),
    ("news", "News"),
    ("romance", "Romance"),
    ("romantic-comedy", "Romantic Comedy"),
    ("science Fiction", "Science Fiction"),
    ("thriller", "Thriller"),
    ("western", "Western"),
)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    year = models.IntegerField()
    length = models.IntegerField(default=0, blank=True, help_text="In minutes")
    synopsis = models.TextField(blank=True, default="")
    image = models.ImageField(upload_to="movies/", blank=True, default="")
    poster = models.ImageField(upload_to="poster/", blank=True, default="")
    trailer_url = models.URLField(blank=True, default="")
    full_url = models.URLField(blank=True, default="")
    facebook_url = models.URLField(blank=True, default="")
    publish = models.BooleanField(default=True)
    imdb = models.URLField(blank=True, default="")
    genre = models.CharField(blank=True, default="", choices=GENRES, max_length=255)
    credits = models.TextField(blank=True, default="")
    story = models.TextField(blank=True, default="")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie", args=[self.slug,])

    @property
    def bragging_rights(self):
        events = self.show_set.prefetch_related("awards").order_by("date")
        rights = []
        for event in events:
            if event.event_type == "festival":
                if event.awards.count():

                    wins = event.awards.filter(status=1).values_list("title", flat=True)
                    if wins:
                        right = "Won **{}** at the {}".format(", ".join(wins), event.title)
                        rights.append(right)

                    nominations = event.awards.filter(status=0).values_list("title", flat=True)
                    if nominations:
                        right = "Nominated for **{}** at the {}".format(", ".join(nominations), event.title)
                        rights.append(right)

                else:
                    right = "Official selection {}".format(event.title)
                    rights.append(right)
            else:
                txt = "%(type)s at %(venue)s in %(city)s" % {
                    "type": event.get_event_type_display(),
                    "venue": event.venue,
                    "city": event.city,
                }
                rights.append(txt)
        return rights

    @property
    def credits_list(self):
        return filter(lambda x: len(x) > 0, self.credits.split("\r\n"))

    @property
    def trailer_embed_url(self):
        return vimeo_embed_url(self.trailer_url)

    @property
    def movie_embed_url(self):
        return vimeo_embed_url(self.full_url)

    @property
    def trailer_share_text(self):
        return "The trailer for {} looks awesome!".format(self.title)

    @property
    def movie_share_text(self):
        return "I just saw {}. It kind of rocked. Go watch it now!".format(self.title)



class Show(models.Model):

    TYPES = (
        ('premiere', 'Premiered'),
        ('festival', 'Film Festival'),
        ('show', 'Screened'),
    )

    title = models.CharField(max_length=255, default="")
    date = models.DateField(blank=True, null=True)
    event_type = models.CharField(max_length=255, verbose_name="Type", choices=TYPES)
    city = models.CharField(max_length=255, default="")
    venue = models.CharField(max_length=255, default="")
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return "{} ({})".format(self.title, self.movie.title)


class Award(models.Model):
    LEVELS = (
        (0, "Nominated"),
        (1, "Winner"),
        (2, "Official Selection"),
    )
    title = models.CharField(max_length=255)
    status = models.IntegerField(choices=LEVELS)
    movie = models.ForeignKey(Movie)
    event = models.ForeignKey(Show, blank=True, null=True, related_name='awards')

    def __str__(self):
        return self.title

