from django.urls import path
from .views import category,createPost
urlpatterns = [
  path('category/',category,name="category"),
  path('create-post/',createPost,name='createpost'),
]
