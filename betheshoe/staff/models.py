from django.db import models
from easy_thumbnails.files import get_thumbnailer


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

    def get_thumb(self):
        if self.image:
            src = get_thumbnailer(self.image).get_thumbnail({'size': (100, 100), }).url
            return u'<img src="{}">'.format(src)
        return ""
    get_thumb.verbose_name = "Foo"
    get_thumb.allow_tags = True



class SocialProfile(models.Model):

    ICON_MAPPINGS = {
        "imdb": dict(icon="fa-film", name="IMDB"),
        "website": dict(icon="fa-cloud", name="Website"),
        "portfolio": dict(icon="fa-cloud", name="Portfolio"),
        "blog": dict(icon="fa-cloud", name="Blog"),
        "email": dict(icon="fa-envelope-alt", name="Email"),
        "facebook": dict(icon="fa-facebook-square", name="Facebook"),
        "twitter": dict(icon="fa-twitter", name="Twitter"),
        "linkedin": dict(icon="fa-linkedin", name="LinkedIn"),
        "youtube": dict(icon="fa-linkedin", name="YouTube"),
        "Flickr": dict(icon="fa-flickr", name="Flickr"),
    }

    ICONS = [(key, ICON_MAPPINGS[key]['name']) for key in ICON_MAPPINGS]

    staffer = models.ForeignKey(Staffer)
    url = models.URLField()
    icon = models.CharField(max_length=255, choices=ICONS)

    def get_icon_class(self):
        return self.ICON_MAPPINGS[self.icon]['icon']

    def __unicode__(self):
        return "{}'s {}".format(self.staffer, self.get_icon_display())

