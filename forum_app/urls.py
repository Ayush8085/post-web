from django.urls import path
from . import views

urlpatterns = [
    path('', views.forums, name='forums'),
    path('create-post/', views.createPost, name='create-post'),
    path('post/<str:pk>/', views.post, name='post'),
]
