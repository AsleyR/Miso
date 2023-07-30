from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

from category.models import Category

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = CloudinaryField("Image", overwrite=True, format="jpg")
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta():
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        to_assign = slugify(self.name)

        # In the case an object with the same name already exists
        if Item.objects.filter(slug=to_assign).exists():
            to_assign = to_assign + str(Item.objects.all().count())

        self.slug = to_assign

        super().save(*args, **kwargs)