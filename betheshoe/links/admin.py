from django.contrib import admin

from .models import Link

class LinkAdmin(admin.ModelAdmin):
    model = Link
    list_display = ["title", "get_absolute_url"]

admin.site.register(Link, LinkAdmin)