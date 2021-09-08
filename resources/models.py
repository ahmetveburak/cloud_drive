from datetime import timedelta

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext as _
from martor.models import MartorField

from resources.validators import file_size_validator


class Post(models.Model):
    title = models.CharField(_("Post Title"), max_length=100)
    slug = models.SlugField(max_length=200, null=True)
    content = MartorField(_("Post Content"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(_("Private"), default=False)
    token = models.ManyToManyField(
        "tokens.Token",
        related_name="%(class)s_tokens",
        verbose_name=_("URL Token"),
        blank=True,
    )

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.id, "slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_token_count(self) -> int:
        return len(self.token.all())

    def is_recent(self) -> bool:
        time_delta: timedelta = timezone.now() - self.created
        if time_delta.total_seconds() < 3:
            return True
        return False


class File(models.Model):
    name = models.CharField(_("File Name"), max_length=100, blank=True)
    slug = models.SlugField(max_length=200, null=True)
    file = models.FileField(upload_to="files", validators=[file_size_validator])
    created = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(_("Private"), default=False)
    is_deleted = models.BooleanField(_("Deleted"), default=False)
    token = models.ManyToManyField(
        "tokens.Token",
        related_name="%(class)s_tokens",
        verbose_name=_("URL Token"),
        blank=True,
    )

    def save(self, *args, **kwargs) -> None:
        if not self.name:
            self.name = self.file.name
        self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("file-detail", kwargs={"pk": self.id, "slug": self.slug})

    def get_token_count(self) -> int:
        return len(self.token.all())

    def is_recent(self) -> bool:
        time_delta: timedelta = timezone.now() - self.created
        if time_delta.total_seconds() < 3:
            return True
        return False
