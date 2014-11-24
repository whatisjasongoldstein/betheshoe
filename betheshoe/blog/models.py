from django.db import models
from django.core.urlresolvers import reverse
from cropper.models import CroppableImageMixin
from cropper.helpers import get_cropped_image

from draftin.models import Draft


class Post(CroppableImageMixin, Draft):
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
        
    def get_absolute_url(self):
        return reverse('blog.post', kwargs={"slug": self.slug})

    @property
    def cropped_image(self):
        crop = get_cropped_image(self, 'image')
        return crop or self.image
