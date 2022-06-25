from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from I4G033993TR5.blog.models import Post

# Create your views here.
class PostListView(ListView):
  model = Post
class PostCreateView(CreateView):
  model = Post
  fields = "__all__"
  success_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):
  model = Post

class PostDeleteView(UpdateView):
  model = Post
  fields = "__all__"
  success_url = reverse_lazy("blog:all")