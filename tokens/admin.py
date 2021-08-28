from django.contrib import admin
from resources.models import Post

from tokens.models import Token

# class PostInline(admin.StackedInline):
#     model = Post


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):

    # inlines = (PostInline,)
    pass
