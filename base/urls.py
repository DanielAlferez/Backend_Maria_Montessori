from django.urls import path
from base import views

urlpatterns = [
    path('posts/', views.get_posts , name='posts'),
    path('post/<str:pk>', views.get_post, name="post"),
    path('category/<str:pk>', views.get_category, name="category"),
    path('create-post/', views.CrearPost.as_view(), name="crear")
]