from django.urls import path
from blog.views import post_list, post_detail, post_new, post_edit, post_delete, post_status, published_post, categories

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/post_status/', post_status, name='post_status'),
    path('post/category/<int:category_pk>', categories, name='categories'),
    path('post/detail/<int:post_pk>', post_detail, name='post_detail'),
    path('post/edit/<int:post_pk>', post_edit, name='post_edit'),
    path('post/published/<int:post_pk>', published_post, name='published_post'),
    path('post/delete/<int:post_pk>', post_delete, name='post_delete'),
    path('post/new', post_new, name='post_new'),
]