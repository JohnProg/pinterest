from django.contrib import admin

from .models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'image_profile', 'about_me', 'website')

    def image_profile(self, user):
        url = user.get_url_image()
        tag = "<img width='150' src='%s'>" % url
        return tag

    image_profile.allow_tags = True

admin.site.register(MyUser, MyUserAdmin)