from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models

from item.models import Item

# Create your models here.

class Cart(models.Model):
    name = models.CharField(max_length=255)
    cart_items = ArrayField(models.CharField(max_length=255))
    created_by = models.ForeignKey(User, related_name='carts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        username = self.created_by.get_username()

        # assign cart name
        self.name = f"{username[0].upper()}{username[1:]}'s cart"

        super().save(*args, **kwargs)