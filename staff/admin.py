from django.contrib import admin
from .models import Group, SocialProfile, Staffer

class SocialProfileInline(admin.TabularInline):
    model = SocialProfile
    extra = 1

class StafferAdmin(admin.ModelAdmin):
    model = Staffer
    inlines = [SocialProfileInline,]
    list_display = ["display_name", "publish", "group", "order"]
    list_editable = ["publish", "order", "group",]

class GroupAdmin(admin.ModelAdmin):
    models = Group
    list_display = ["title", "staff_list", "order"]
    list_editable = ["order",]
    ordering = ("order", )


admin.site.register(Staffer, StafferAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(SocialProfile)
