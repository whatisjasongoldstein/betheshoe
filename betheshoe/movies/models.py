from django.db import models
from django.core.urlresolvers import reverse

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
    publish = models.BooleanField(default=True)
    imdb = models.URLField(blank=True, default="")
    genre = models.CharField(blank=True, default="", choices=GENRES, max_length=255)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie", args=[self.slug,])

    def get_bragging_rights(self):
        rights = []
        festivals = self.show_set.filter(event_type="festival").prefetch_related("awards")
        for festival in festivals:
            if festival.awards.count():

                wins = festival.awards.filter(status=1).values_list("title", flat=True)
                if wins:
                    right = "Won {} at the {}".format(", ".join(wins), festival.title)
                    rights.append(right)

                nominations = festival.awards.filter(status=0).values_list("title", flat=True)
                if nominations:
                    right = "Nominated for {} at the {}".format(", ".join(nominations), festival.title)
                    rights.append(right)

            else:
                right = "Official selection {}".format(festival.title)
                rights.append(right)
        return rights


    def get_nonfestival_events(self):
        shows = self.show_set.exclude(event_type="festival").order_by('-date')
        notes = []
        for show in shows:
            txt = "{type} at {venue} in {city}, {state}".format(**{
                    "type": show.get_event_type_display(),
                    "venue": show.venue,
                    "city": show.city,
                    "state": show.state,
                })
            notes.append(txt)
        return notes


    @property
    def trailer_embed(self):
        return get_embed_src(self.trailer_url)

    @property
    def movie_embed(self):
        return get_embed_src(self.full_url)

    @property
    def trailer_share_text(self):
        return "The trailer for {} looks awesome!".format(self.title)

    @property
    def movie_share_text(self):
        return "I just saw {}. It kind of rocked. Go watch it now!".format(self.title)



class Show(models.Model):

    TYPES = (
        ('premiere', 'Premiere'),
        ('festival', 'Film Festival'),
        ('show', 'Screening'),
    )

    title = models.CharField(max_length=255, default="")
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    slug = models.SlugField()
    summary = models.TextField(verbose_name="Description", blank=True, null=True)
    event_type = models.CharField(max_length=255, verbose_name="Type", choices=TYPES)
    city = models.CharField(max_length=255, default="")
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
    event = models.ForeignKey(Show, blank=True, null=True, related_name='awards')

    def __unicode__(self):
        return self.title

    def get_bragging_rights(self):
        txt = "{} {}".format(self.get_status_display(), self.title)
        if self.event:
            txt += " at {}".format(self.event.title)
        return txt

