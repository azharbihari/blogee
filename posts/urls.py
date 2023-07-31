from django.urls import path
from posts.views import PostListView, PostDetailView, CommentDeleteView, CommentUpdateView, CommentCreateView, CategoryDetailView, PostMonthArchiveView

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("<slug:slug>/", PostDetailView.as_view(), name="post-detail"),
    path("<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
    path("<int:pk>/edit/", CommentUpdateView.as_view(), name="comment-edit"),
    path("<slug:slug>/add/", CommentCreateView.as_view(), name="comment-add"),
    path("category/<slug:slug>/",
         CategoryDetailView.as_view(), name="category-detail"),
    path(
        "<int:year>/<str:month>/", PostMonthArchiveView.as_view(), name="post-month-archive",
    ),
]
