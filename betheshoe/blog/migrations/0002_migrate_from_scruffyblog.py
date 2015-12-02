# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import markdown
from django.db import models, migrations
from django.contrib.contenttypes.models import ContentType

def update_crops():
    try:
        from cropper.models import Crop
    except ImportError:
        logging.warning("Scruffy Cropper is no longer installed. Migration won't update images.")
        return False

    post_ct = ContentType.objects.get(app_label="blog", model="post")
    scruffy_post_ct = ContentType.objects.get(app_label="scruffy_blog", model="post")
    scruffy_post_image_ct = ContentType.objects.get(app_label="scruffy_blog", model="postimage")

    Crop.objects.filter(content_type=scruffy_post_ct).update(content_type=post_ct)

    # Won't work unless scruffy blog still exists
    img_cls = scruffy_post_image_ct.model_class()
    img_dict = img_cls.objects.all().values("id", "post_id")
    for img in img_dict:
        Crop.objects.filter(
            content_type=scruffy_post_ct, object_id=img["id"]
        ).update(content_type=post_ct, object_id=img["post_id"])



def import_posts(apps, schema_editor):

    try:
        from scruffy_blog.models import Post as ScruffyPost
    except ImportError:
        logging.warning("Scruffy Blog is no longer installed. Migration won't run.")
        return False

    DraftPost = apps.get_model("blog", "post")
    Collection = apps.get_model("draftin", "collection")
    Staffer = apps.get_model("staff", "Staffer")

    staff = Staffer.objects.all().values("id","first_name", "last_name")
    staff_fullname_map = {" ".join([s["first_name"], s["last_name"]]): s["id"] for s in staff}

    collection = Collection.objects.latest("id")

    for old_post in ScruffyPost.objects.all():

        elements = old_post.postelement_set.filter(obj_type='text').order_by('order')
        markdown = "\n\n".join([element.content for element in elements])

        post = DraftPost(
            pk = old_post.id,
            title = old_post.title,
            subtitle = old_post.subtitle,
            slug = old_post.slug,
            image = old_post.image,
            is_thumbnail = old_post.is_thumbnail,
            author_id = staff_fullname_map.get(old_post.author, None),
            date_published = old_post.date,

            # Draft fields
            name = old_post.title,
            collection = collection,
            draft_id = 0,
            content = markdown,
            content_html = old_post.cached_html,
            draftin_user_id = 0,
            draftin_user_email = "",
            created_at = old_post.date,
            updated_at = old_post.date,
            published = old_post.published,
        )
        post.save()
    
    update_crops()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_posts),
    ]