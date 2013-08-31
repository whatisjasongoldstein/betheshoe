from django.db import models

class Staffer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="staff/")
    bio = models.TextField(blank=True, default="")
    publish = models.IntegerField(default=0)
    order = models.IntegerField(default=0)


class SocialProfile(models.Model):

    ICONS = (
        ('icon-envelope-alt', "Email"),
        ('icon-facebook', "Facebook"),
        ('icon-twitter', "Twitter"),
        ('icon-linkedin', "LinkedIn"),
        ('icon-youtube', "YouTube"),
        ('icon-flickr', "Flickr"),
    )

    staffer = models.ForeignKey(Staffer)
    url = models.URLField()
    icon = models.CharField(max_length=255, choices=ICONS)

