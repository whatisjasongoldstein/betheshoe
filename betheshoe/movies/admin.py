from django.contrib import admin
from .models import Award, Movie, Show

class ShowInline(admin.StackedInline):
    model = Show
    extra = 0

class AwardInline(admin.StackedInline):
    model = Award
    extra = 0

class MovieAdmin(admin.ModelAdmin):
    model = Movie
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ShowInline, AwardInline]
    list_display = ["title", "year", "publish", "genre"]
    list_editable = ["year", "publish", "genre"]
    ordering = ("-year",)

class AwardAdmin(admin.ModelAdmin):
    model = Award
    list_display = ["title", "event", "get_status_display"]

class ShowAdmin(admin.ModelAdmin):
    model = Show


admin.site.register(Award, AwardAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Show, ShowAdmin)