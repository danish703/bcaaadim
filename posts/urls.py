from django.urls import path
from .views import category,createPost,posts
urlpatterns = [
  path('',posts,name="posts"),
  path('category/',category,name="category"),
  path('create-post/',createPost,name='createpost'),
]
