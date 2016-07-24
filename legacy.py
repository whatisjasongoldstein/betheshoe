# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlogPost(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255)
    image = models.CharField(max_length=100)
    is_thumbnail = models.BooleanField()
    author = models.ForeignKey('StaffStaffer', models.DO_NOTHING, blank=True, null=True)
    draft = models.ForeignKey('DraftinDraft', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'blog_post'


class CropperCrop(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    field = models.CharField(max_length=255)
    image = models.CharField(max_length=100)
    coordinates = models.TextField()

    class Meta:
        managed = False
        db_table = 'cropper_crop'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoFeaturingDashboard(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    slug = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'django_featuring_dashboard'


class DjangoFeaturingDashboardSites(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    dashboard = models.ForeignKey(DjangoFeaturingDashboard, models.DO_NOTHING)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_featuring_dashboard_sites'
        unique_together = (('dashboard', 'site'),)


class DjangoFeaturingThing(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    order = models.IntegerField()
    object_id = models.PositiveIntegerField()
    template = models.CharField(max_length=255)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    dashboard = models.ForeignKey(DjangoFeaturingDashboard, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_featuring_thing'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    domain = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'django_site'


class DraftinCollection(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    auto_publish = models.BooleanField()
    uuid = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'draftin_collection'


class DraftinDraft(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    draft_id = models.IntegerField()
    name = models.CharField(max_length=512)
    content = models.TextField()
    content_html = models.TextField()
    draftin_user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    last_synced_at = models.DateTimeField()
    collection = models.ForeignKey(DraftinCollection, models.DO_NOTHING)
    published = models.BooleanField()
    date_published = models.DateTimeField(blank=True, null=True)
    draftin_user_email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'draftin_draft'


class EasyThumbnailsSource(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_source'
        unique_together = (('storage_hash', 'name'),)


class EasyThumbnailsThumbnail(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()
    source = models.ForeignKey(EasyThumbnailsSource, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_thumbnail'
        unique_together = (('storage_hash', 'name', 'source'),)


class LinksLink(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=200)
    kicker = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'links_link'


class MoviesAward(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=255)
    status = models.IntegerField()
    event = models.ForeignKey('MoviesShow', models.DO_NOTHING, blank=True, null=True)
    movie = models.ForeignKey('MoviesMovie', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movies_award'


class MoviesMovie(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=50)
    length = models.IntegerField()
    synopsis = models.TextField()
    image = models.CharField(max_length=100)
    poster = models.CharField(max_length=100)
    trailer_url = models.CharField(max_length=200)
    full_url = models.CharField(max_length=200)
    publish = models.BooleanField()
    imdb = models.CharField(max_length=200)
    genre = models.CharField(max_length=255)
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'movies_movie'


class MoviesShow(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    slug = models.CharField(max_length=50)
    summary = models.TextField(blank=True, null=True)
    event_type = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    venue = models.CharField(max_length=255)
    venue_link = models.CharField(max_length=200)
    facebook_event = models.CharField(max_length=200)
    movie = models.ForeignKey(MoviesMovie, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movies_show'


class MusicLink(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    url = models.CharField(max_length=200)
    icon = models.CharField(max_length=255)
    musician = models.ForeignKey('MusicMusician', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'music_link'


class MusicMusician(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=255)
    hometown = models.CharField(max_length=255)
    image = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField()
    publish = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'music_musician'


class MusicMusicianMovies(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    musician = models.ForeignKey(MusicMusician, models.DO_NOTHING)
    movie = models.ForeignKey(MoviesMovie, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'music_musician_movies'
        unique_together = (('musician', 'movie'),)


class StaffGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=255)
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'staff_group'


class StaffSocialprofile(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    url = models.CharField(max_length=200)
    icon = models.CharField(max_length=255)
    staffer = models.ForeignKey('StaffStaffer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'staff_socialprofile'


class StaffStaffer(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.CharField(max_length=100)
    bio = models.TextField()
    publish = models.BooleanField()
    order = models.IntegerField()
    group = models.ForeignKey(StaffGroup, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_staffer'
