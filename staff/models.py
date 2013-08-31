from django.db import models

class Group(models.Model):
    title = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    def staff_list(self):
        return ", ".join([person.display_name for person in self.staffer_set.filter(publish=True)])


class Staffer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="staff/", blank=True, default="")
    bio = models.TextField(blank=True, default="")
    publish = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    group = models.ForeignKey(Group, null=True)

    def __unicode__(self):
        return self.display_name

    @property
    def display_name(self):
        return "{} {}".format(self.first_name, self.last_name)



class SocialProfile(models.Model):

    ICONS = (
        ('icon-cloud', "Website"),
        ('icon-film', "IMDB"),
        ('icon-envelope-alt', "Email"),
        ('icon-facebook-sign', "Facebook"),
        ('icon-twitter', "Twitter"),
        ('icon-linkedin', "LinkedIn"),
        ('icon-youtube', "YouTube"),
        ('icon-flickr', "Flickr"),
    )

    staffer = models.ForeignKey(Staffer)
    url = models.URLField()
    icon = models.CharField(max_length=255, choices=ICONS)

