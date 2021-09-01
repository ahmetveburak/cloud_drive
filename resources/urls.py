from django.contrib.auth import views as auth_views
from django.urls import path

from resources.views import file, post

# app_name = "resources"

urlpatterns = [
    path("", file.FileTokenCreate.as_view(), name="index"),
    path("post/new", post.PostCreateView.as_view(), name="post-create"),
    path("post/<slug:slug>/", post.PostDetailView.as_view(), name="post-detail"),
    path("post/edit/<int:pk>/", post.PostEditView.as_view(), name="post-edit"),
    path("posts/", post.PostListView.as_view(), name="post-list"),
    path("file/new", file.FileCreateView.as_view(), name="file-create"),
    path("file/<slug:slug>/", file.FileDetailView.as_view(), name="file-detail"),
    path("file/edit/<int:pk>/", file.FileEditView.as_view(), name="file-edit"),
    path("files/", file.FileListView.as_view(), name="file-list"),
    path("login/", auth_views.LoginView.as_view(template_name="resources/registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="resources/registration/logout.html"), name="logout"),
]
