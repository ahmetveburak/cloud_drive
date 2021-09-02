from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.views.generic import CreateView, DetailView, TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from resources.forms import FileCreateForm
from resources.models import File
from tokens.forms import TokenCreateForm
from tokens.models import Token


class FileCreateView(CreateView):
    template_name = "resources/file/file_create.html"
    model = File
    fields = ("name", "file", "is_private")


class FileTokenCreate(TemplateView):
    template_name = "resources/index.html"

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["file_form"] = FileCreateForm(prefix="file")
        context["token_form"] = TokenCreateForm(prefix="token")

        return context

    def post(self, *args, **kwargs):
        # handling file in post request
        # https://stackoverflow.com/a/8542030/12306993

        data = self.request.POST
        file = self.request.FILES["file-file"]

        file_name = data.get("file-name")
        is_private = True if data.get("file-is_private") else False

        new_file = File(name=file_name, file=file, is_private=is_private)
        new_file.save()

        file_url = reverse("file-detail", kwargs={"slug": new_file.slug})

        if is_private:
            exp_date = data.get("token-enabled_to")
            if exp_date:
                exp_date = timezone.make_aware(parse_datetime(exp_date))

            exp_count = data.get("token-enabled_count")

            new_token = Token(
                enabled_count=int(exp_count) + 1 if exp_count else 0,
                enabled_to=exp_date if exp_date else None,
            )
            new_token.save()
            new_file.token.add(new_token)

            return redirect(f"{file_url}?token={new_token.token}")

        return redirect(file_url)


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


class FileEditView(UpdateView):
    template_name = "resources/file/file_create.html"
    model = File
    fields = ("name", "file", "is_private", "token")

    def get_absolute_url(self):
        return reverse_lazy("file-detail", kwargs={"slug": self.slug})


class FileListView(LoginRequiredMixin, ListView):
    template_name = "resources/file/file_list.html"
    model = File
