from django.urls import path

from resources import views

app_name = "resources"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("post/new", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("file/new", views.FileCreateView.as_view(), name="file-create"),
    path("file/<int:pk>/", views.FileDetailView.as_view(), name="file-detail"),
]
