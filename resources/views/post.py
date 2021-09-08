from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from resources.forms import PostCreateForm
from resources.models import Post
from resources.utils import add_token
from tokens.forms import TokenCreateForm


class PostCreateView(CreateView):
    template_name = "resources/post/post_create.html"
    model = Post
    fields = ("title", "content", "is_private")

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["post_form"] = PostCreateForm(prefix="post")
        context["token_form"] = TokenCreateForm(prefix="token")
        return context

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        data = request.POST

        post_title = data.get("post-title")
        post_content = data.get("post-content")

        is_private = bool(data.get("file-is_private"))
        new_post = Post(title=post_title, content=post_content, is_private=is_private)
        new_post.save()

        post_url = reverse("post-detail", kwargs={"pk": new_post.id, "slug": new_post.slug})

        if is_private:
            new_token = add_token(new_post, data)
            return redirect(f"{post_url}?token={new_token.token}")

        return redirect(post_url)


class PostDetailView(DetailView):
    template_name = "resources/post/post_detail.html"
    model = Post

    def get_object(self, queryset=None):
        obj: Post = super(PostDetailView, self).get_object(queryset=queryset)

        if self.request.user.is_authenticated:
            return obj

        if obj.is_private:
            url_token = self.request.GET.get("token")
            query = {"token": url_token, "is_enabled": True}
            token = get_object_or_404(obj.token.all(), **query)
            if token.is_accessible():
                return obj
            raise Http404("You are not allowed.")
        return obj


class PostDetailAdminView(LoginRequiredMixin, PostDetailView):
    pass


class PostEditView(LoginRequiredMixin, UpdateView):
    template_name = "resources/post/post_create.html"
    model = Post
    fields = ("title", "content", "is_private", "token")

    def get_absolute_url(self):
        return reverse_lazy("post-detail", kwargs={"slug": self.slug})


class PostListView(LoginRequiredMixin, ListView):
    template_name = "resources/post/post_list.html"
    model = Post
