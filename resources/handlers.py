from django.shortcuts import redirect
from django.urls.base import reverse


def view_404(request, *args, **kwargs):
    print("tst")
    return redirect(f'{reverse("index")}?notfound=ok')
