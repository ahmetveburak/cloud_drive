from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from resources.models import File, Post


class PostCreateView(CreateView):
    template_name = "resources/post/post_create.html"
    model = Post
    fields = ("title", "content", "is_private", "token")


class PostDetailView(DetailView):
    template_name = "resources/post/post_detail.html"
    model = Post

    def get_object(self, queryset=None):
        obj: Post = super(PostDetailView, self).get_object(queryset=queryset)

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


class PostEditView(UpdateView):
    template_name = "resources/post/post_create.html"
    model = Post
    fields = ("title", "content", "is_private", "token")

    def get_absolute_url(self):
        return reverse_lazy("post-detail", kwargs={"slug": self.slug})


class PostListView(LoginRequiredMixin, ListView):
    template_name = "resources/post/post_list.html"
    model = Post
