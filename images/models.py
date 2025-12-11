from urllib import request
from django.core.files.base import ContentFile
from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.


class Image(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="images_created",
        on_delete=models.CASCADE,
    )

    title = models.CharField(max_length=150)

    slug = models.SlugField(max_length=200, blank=True)

    url = models.URLField()

    description = models.TextField(blank=True)

    image = models.ImageField(upload_to="images/%Y/%m/%d/")

    created = models.DateTimeField(auto_now_add=True, db_index=True)

    users_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="images_liked", blank=True
    )

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'

        # download image
        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)

        if commit:
            image.save()
        return image

    def __str__(self):

        return self.title
