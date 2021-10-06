from django.views.generic.base import View
from blog.views import PostListView
from django.urls import path
from .views import(
            #post_list, 
            #post_detail, 
            #post_create, 
            PostCreateView,
            #post_update, 
            #post_delete, 
            PostListView,
            PostDetailView,
            PostCreateView,
            PostUpdateView,
            PostDeleteView
            )

app_name = 'blog'
urlpatterns = [
    # path('', post_list, name='post_list'),
    path('<slug:get_slug>/update', PostUpdateView.as_view(), name='post_update'),
    path('<slug:get_slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('', PostListView.as_view(), name="post_list"),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<slug:get_slug>/', PostDetailView.as_view(), name='post_detail'),
]
