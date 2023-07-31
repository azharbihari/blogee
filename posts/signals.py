from django.db.models.signals import post_save, pre_delete, pre_save, post_delete
from django.dispatch import receiver
from posts.models import Post
import os
from PIL import Image


@receiver(pre_save, sender=Post)
def delete_changed_featured_image_on_save(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = Post.objects.get(pk=instance.pk)
            if old_instance.featured_image != instance.featured_image:
                if old_instance.featured_image != 'featured_images/default_featured_image.svg':
                    old_instance.featured_image.delete(save=False)
        except Post.DoesNotExist:
            pass


@receiver(pre_delete, sender=Post)
def delete_featured_image_on_delete(sender, instance, **kwargs):
    if instance.featured_image and instance.featured_image != 'featured_images/default_featured_image.svg':
        instance.featured_image.delete(save=False)
