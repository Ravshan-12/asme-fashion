from django.db import models
from django.shortcuts import reverse

from blog_model import BaseModel
from catalogues.models import Category


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    image = models.ImageField(upload_to='product_media/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)

    def get_detail_url(self):
        return reverse(
            'articles:detail',
            kwargs={
                'year': self.posted_at.year,
                'month': self.posted_at.month,
                'day': self.posted_at.day,
                'slug': self.slug,
            }
        )


