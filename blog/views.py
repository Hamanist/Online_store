from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    extra_context = {'title': 'Блог'}

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_sign=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {'title': 'Описание Блога'}

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('blog:list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('blog:list')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
