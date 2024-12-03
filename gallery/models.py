from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class GalleryGroup(models.Model):

    title = models.CharField(max_length=100, default='')
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  # Solo generar el slug si está vacío
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('gallery.views.gallery_detail', args=[str(self.id)])


class Artwork(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    art = models.ImageField(upload_to="art")
    gallery_group = models.ForeignKey('GalleryGroup', on_delete=models.CASCADE)
    
    def artwork_upload_path(instance, filename):
        return f'artworks/{instance.group.slug}/{filename}'

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery_detail', args=[str(self.id)])
