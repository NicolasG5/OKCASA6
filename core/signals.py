from django.contrib.auth.models import User, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def assign_permissions_to_client(sender, instance, created, **kwargs):
    if created and instance.is_active:
        perm = Permission.objects.get(codename='cliente_access')
        instance.user_permissions.add(perm)