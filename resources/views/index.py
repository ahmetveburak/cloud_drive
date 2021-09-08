from typing import Any, Dict

from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView
from resources.forms import FileCreateForm
from resources.models import File
from resources.utils import add_token
from tokens.forms import TokenCreateForm


class IndexView(TemplateView):
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
        is_private = bool(data.get("file-is_private"))

        new_file = File(name=file_name, file=file, is_private=is_private)
        new_file.save()

        file_url = reverse("file-detail", kwargs={"pk": new_file.id, "slug": new_file.slug})

        if is_private:
            new_token = add_token(new_file, data)
            return redirect(f"{file_url}?token={new_token.token}")

        return redirect(file_url)
