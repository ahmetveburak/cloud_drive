from django.urls import path

from resources.views import file, index, post

# app_name = "resources"

urlpatterns = [
    path("", index.IndexView.as_view(), name="index"),
    path("post/new", post.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/<slug:slug>/", post.PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/", post.PostDetailAdminView.as_view(), name="post-detail-admin"),
    path("post/edit/<int:pk>/", post.PostEditView.as_view(), name="post-edit"),
    path("posts/", post.PostListView.as_view(), name="post-list"),
    #
    path("file/new", file.FileCreateView.as_view(), name="file-create"),
    path("file/<int:pk>/<slug:slug>/", file.FileDetailView.as_view(), name="file-detail"),
    path("file/<int:pk>/", file.FileDetailAdminView.as_view(), name="file-detail-admin"),
    path("file/edit/<int:pk>/", file.FileEditView.as_view(), name="file-edit"),
    path("files/", file.FileListView.as_view(), name="file-list"),
]
