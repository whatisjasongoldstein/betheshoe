from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from cropper.models import CroppableImageMixin
from cropper.helpers import get_cropped_image

from draftin.models import Draft


class Post(CroppableImageMixin, models.Model):
    draft = models.OneToOneField(Draft, editable=False)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, help_text="looks-like-this-and-should-never-change", unique=True)
    author = models.ForeignKey("staff.Staffer", blank=True, null=True)
    image = models.ImageField(upload_to="blog/%Y/%m", blank=True, default="", 
        help_text="Lead image. If this is not selected, the first visual in the body will be used.")
    is_thumbnail = models.BooleanField("Thumbnail only", blank=True, default=False,
        help_text="The image is only for thumbnails, don't use it as lead art.")

    def __unicode__(self):
        return self.title or self.name

    draft_properties = [
        "content",
        "content_html",
        "created_at",
        "updated_at",
        "published",
        "date_published",
        "name",
    ]
        
    def get_absolute_url(self):
        return reverse('blog.post', kwargs={"slug": self.slug})

    @property
    def cropped_image(self):
        crop = get_cropped_image(self, 'image')
        return crop or self.image

    def __getattr__(self, key, *args):
        """
        Bullshit-free concrete inheritance.
        Fall back on the property check, but
        don't do anything crazy in the database
        or break signals.
        """
        if key in self.draft_properties:
            return getattr(self.draft, key)
        return super(Post, self).__getattribute__(key, *args)


def create_posts_with_drafts(**kwargs):
    """
    Create a post any time a Draft is received.
    """
    obj = kwargs.get("instance", None)
    Post.objects.get_or_create(draft=obj, defaults={
        "title": obj.name,
        "slug": slugify(obj.name),
    })

models.signals.post_save.connect(create_posts_with_drafts, sender=Draft)

