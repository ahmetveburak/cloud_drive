from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from resources.models import File


class FileCreateView(CreateView):
    template_name = "resources/file/file_create.html"
    model = File
    fields = ("name", "file", "is_private")


class FileDetailView(DetailView):
    template_name = "resources/file/file_detail.html"
    model = File

    def get_object(self, queryset=None):
        obj: File = super(FileDetailView, self).get_object(queryset=queryset)

        if self.request.user.is_authenticated:
            return obj

        if obj.is_private:
            url_token = self.request.GET.dict().get("token")
            query = {"token": url_token, "is_enabled": True}
            token = get_object_or_404(obj.token.all(), **query)
            if token.is_accessible():
                return obj
            raise Http404("You are not allowed.")
        return obj


class FileDetailAdminView(LoginRequiredMixin, FileDetailView):
    pass


class FileEditView(LoginRequiredMixin, UpdateView):
    template_name = "resources/file/file_create.html"
    model = File
    fields = ("name", "file", "is_private", "token")

    def get_absolute_url(self):
        return reverse_lazy("file-detail", kwargs={"slug": self.slug})


class FileListView(LoginRequiredMixin, ListView):
    template_name = "resources/file/file_list.html"
    model = File
