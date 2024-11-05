# blog/urls.py
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list_view, name="post_list_view"),
    path(
        "category/<str:category_name>/", views.post_list_view, name="post_list_category"
    ),
    path(
        "author/<int:author_id>/", views.post_list_view, name="posts_by_author"
    ),  # New URL pattern for author filter
    path("<int:post_id>/", views.post_detail_view, name="post_detail_view"),
]
