from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, DetailView
from django.views.generic.base import TemplateResponseMixin, View

from resources.forms import FileForm
from resources.models import File, Post


class IndexView(TemplateResponseMixin, View):
    template_name = "resources/index.html"

    def get(self, *args, **kwargs):
        return render(None, self.template_name)


class PostCreateView(CreateView):
    template_name = "resources/post/post_create.html"
    model = Post
    fields = ("title", "content", "is_private", "token")

    def get_context_data(self, **kwargs):
        a = super().get_context_data(**kwargs)
        print(a)
        return a


class PostDetailView(DetailView):
    template_name = "resources/post/post_detail.html"
    model = Post

    def get_object(self, queryset=None):
        obj: Post = super(PostDetailView, self).get_object(queryset=queryset)
        if obj.is_private:
            url_token = self.request.GET.dict().get("token")
            query = {"token": url_token, "is_enabled": True}
            token = get_object_or_404(obj.token.all(), **query)
            if token.is_accessible():
                return obj
            raise Http404("You are not allowed.")
        return obj


class FileCreateView(CreateView):
    template_name = "resources/file/file_create.html"
    model = File
    fields = "__all__"

    def get_context_data(self, **kwargs):
        a = super().get_context_data(**kwargs)
        print(a)
        return a


class FileDetailView(DetailView):
    template_name = "resources/file/file_detail.html"
    model = File

    def get_object(self, queryset=None):
        obj: File = super(FileDetailView, self).get_object(queryset=queryset)
        if obj.is_private:
            url_token = self.request.GET.dict().get("token")
            query = {"token": url_token, "is_enabled": True}
            token = get_object_or_404(obj.token.all(), **query)
            if token.is_accessible():
                return obj
            raise Http404("You are not allowed.")
        return obj
