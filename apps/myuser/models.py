from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from my_red.settings import MEDIA_URL


class MyUser(models.Model):

    user = models.OneToOneField(
        User
    )
    image = models.ImageField(upload_to='image_profile')
    about_me = models.TextField()
    website = models.URLField(max_length=200)

    def __unicode__(self):
        return self.user.username

    def get_url_image(self):
        return MEDIA_URL + '%s' % self.image

    @receiver(post_save, sender=User)
    def create_favorites(sender, instance, created, **kwargs):
        if created:
            MyUser.objects.create(user=instance)