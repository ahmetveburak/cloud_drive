from typing import Any

from django import forms
from django.contrib import admin
from django.db import models
from django.forms import widgets
from django.http.request import HttpRequest
from django.utils.crypto import get_random_string

from tokens.forms import TokenAdminFrom
from tokens.models import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    form = TokenAdminFrom

    def get_form(self, request: HttpRequest, obj=None, **kwargs: Any):
        form = super().get_form(request, obj=obj, **kwargs)
        form.base_fields["token"].initial = get_random_string(length=32)
        return form
