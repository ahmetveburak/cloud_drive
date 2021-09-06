from django.shortcuts import redirect
from django.urls.base import reverse


def view_404(*args, **kwargs):
    return redirect(f'{reverse("index")}?notfound=ok')
