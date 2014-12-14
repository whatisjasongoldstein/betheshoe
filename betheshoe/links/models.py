from django.db import models

class Link(models.Model):
    """
    Generic link for featuring stuff.
    """
    title = models.CharField(max_length=200)
    kicker = models.CharField(max_length=200, blank=True, default="")
    image = models.ImageField(upload_to="links/%Y/", blank=True, default="")
    url = models.URLField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.url