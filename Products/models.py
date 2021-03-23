from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.utils.safestring import mark_safe
# Create your models here.


class Category(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/')
    status = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

class Product(models.Model):
    category = TreeForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='image/')
    status = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)
        else:
            return 'No Image Found'