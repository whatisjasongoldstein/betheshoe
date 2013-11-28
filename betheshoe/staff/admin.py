from django.contrib import admin
from .models import Group, SocialProfile, Staffer

class SocialProfileInline(admin.TabularInline):
    model = SocialProfile
    extra = 1

class StafferAdmin(admin.ModelAdmin):
    model = Staffer
    inlines = [SocialProfileInline,]
    list_filter = ["group",]
    list_display = ["display_name", "get_thumb", "bio", "publish", "group", "order"]
    list_editable = ["publish", "order", "group", "bio"]
    ordering = ("group__order", "order",)

class GroupAdmin(admin.ModelAdmin):
    models = Group
    list_display = ["title", "staff_list", "order"]
    list_editable = ["order",]
    ordering = ("order",)

class SocialProfileAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "staffer", "icon", "url"]
    list_filter = ["staffer",]
    list_editable = ["icon", "url"]


admin.site.register(Staffer, StafferAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(SocialProfile, SocialProfileAdmin)
