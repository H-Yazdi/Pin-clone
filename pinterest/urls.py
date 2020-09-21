from django.urls import path

from . import views

app_name = "pinterest"

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('like_image/', views.like_image, name='like_image'),
    path('delete/<int:id>/', views.delete_image, name='delete_image'),
    path('my_post/', views.my_post, name='my_post'),
    path('user_post/<int:user_id>/', views.my_post, name='user_post'),
    path('', views.index, name='index'),
]
