from django.contrib import admin
from .models import Musician, Link

class LinkInline(admin.TabularInline):
    model = Link
    extra = 3

class MusicianAdmin(admin.ModelAdmin):
    model = Musician
    list_display = ["name", "hometown", "order"]
    list_editable = ["order",]
    inlines = [LinkInline,]
    filter_horizontal = ["movies",]

admin.site.register(Musician, MusicianAdmin)
admin.site.register(Link)