from django.urls import path

from blog.views import BlogListView, BlogDetailView, BlogCreateView
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('view/<int:pk>', BlogDetailView.as_view(), name='blog_view'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
]
