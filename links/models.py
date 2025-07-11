from django.db import models
from django.utils.text import slugify

# Create your models here.
class Link(models.Model):
    original_url = models.URLField(max_length=200, unique=True)
    short_url = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.original_url} -> {self.short_url}"
    
    def click(self):
        self.clicks += 1
        self.save()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.short_url)
        super().save(*args, **kwargs)