from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    extra_context = {'title': 'Блог'}


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {'title': 'Описание Блога'}


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('blog:list')




