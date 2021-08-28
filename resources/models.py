from django.db import models
from martor.models import MartorField

from resources.validators import file_size_validator


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, null=True)
    content = MartorField()
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)
    token = models.ManyToManyField(
        "tokens.Token", related_name="%(class)s_tokens", verbose_name="URL Token", blank=True
    )

    def __str__(self) -> str:
        return self.title


class File(models.Model):
    name = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to="files", validators=[file_size_validator])
    created = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(default=False)
    token = models.ManyToManyField(
        "tokens.Token", related_name="%(class)s_tokens", verbose_name="URL Token", blank=True
    )

    def save(self, *args, **kwargs) -> None:
        if not self.name:
            self.name = self.file.name
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
