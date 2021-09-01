from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget

from resources.models import File, Post


class PostTokenInline(admin.StackedInline):
    model = Post.token.through
    Post.token.through.__str__ = lambda self: f"/?token={self.token.token}"
    extra = 0
    verbose_name = "token"
    verbose_name_plural = "tokens"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "slug",
        "content",
        "is_private",
    )

    formfield_overrides = {
        models.TextField: {"widget": AdminMartorWidget},
    }

    prepopulated_fields = {"slug": ("title",)}

    inlines = (PostTokenInline,)


class FileTokenInline(admin.StackedInline):
    model = File.token.through
    File.token.through.__str__ = lambda self: f"/?token={self.token.token}"
    extra = 0
    verbose_name = "token"
    verbose_name_plural = "tokens"


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "file",
        "is_private",
    )

    inlines = (FileTokenInline,)
