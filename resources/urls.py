from django.contrib.auth import views as auth_views
from django.urls import path

from resources import views

# app_name = "resources"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("post/new", views.PostCreateView.as_view(), name="post-create"),
    path("post/<slug:slug>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/edit/<int:pk>/", views.PostEditView.as_view(), name="post-edit"),
    path("posts/", views.PostListView.as_view(), name="post-list"),
    path("file/new", views.FileCreateView.as_view(), name="file-create"),
    path("file/<int:pk>/", views.FileDetailView.as_view(), name="file-detail"),
    path("login/", auth_views.LoginView.as_view(template_name="resources/registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="resources/registration/logout.html"), name="logout"),
]
