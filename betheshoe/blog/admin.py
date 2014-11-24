from django import forms
from django.contrib import admin
from django.core.urlresolvers import reverse
from cropper.widgets import CropImageWidget

from .models import Post

class PostForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        # self.redirect_url = kwargs.pop('redirect_url', None) or "/"
        # self.cropper_url = kwargs.pop("cropper_url", None )
        super(PostForm,self).__init__(*args,**kwargs)

        obj = kwargs.get('instance')

        # If there's an instance, we can crop. Otherwise that field is sort of irrelevant anyway.
        crop_attrs={}
        if obj and obj.id:
            self.cropper_url = reverse('crop',kwargs=dict(
                app=self._meta.model._meta.app_label, 
                model=self._meta.model._meta.model_name, 
                obj_id=obj.id, 
                field='image',))
            crop_attrs = {
                'data-crop-url': self.cropper_url, 
                'post-save-redirect': self.redirect_url,
            }

        self.fields['image'] = forms.ImageField(widget=CropImageWidget(attrs=crop_attrs), required=False)
        
    class Meta:
        model = Post



class PostAdmin(admin.ModelAdmin):
    model = Post
    form = PostForm
    list_display = ["title", "subtitle", "draft_admin", "author", "created_at", "published"]
    ordering = ["-id", ]
    readonly_fields = ["draft", ]

    def draft_admin(self, instance=None):
        if instance:
            return '<a href="{url}">{draft_id}</a>'.format(
                    url = reverse("admin:draftin_draft_change", args=[instance.draft.id,]),
                    draft_id = instance.draft.draft_id)
    draft_admin.allow_tags = True

    def published(self, instance=None):
        if instance:
            return instance.draft.published
        return ""

    def created_at(self, instance=None):
        if instance:
            return instance.draft.created_at
        return ""

    def get_form(self, request, obj, fields=None):

        class form_cls(PostForm):
            redirect_url = request.path
            
        return form_cls

admin.site.register(Post, PostAdmin)