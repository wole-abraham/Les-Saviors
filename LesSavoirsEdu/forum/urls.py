from django.urls import path
from .views import forum, Post_comment

urlpatterns = [
    path('', forum, name='forum'),
    path('post/<int:post_id>', Post_comment, name="post_comment"),
]