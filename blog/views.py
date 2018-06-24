from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import BlogForm

from .models import Blog

class BlogListView(ListView):
  model = Blog
  context_object_name = "blogs"
  paginate_by = 3

class BlogDetailView(DetailView):
  model = Blog
  context_object_name = "blog"

class BlogCreateView(LoginRequiredMixin, CreateView):
  model = Blog
  form_class = BlogForm
  template_name = 'blog/blog_create_form.html'
  # fields = ["content",]
  success_url = reverse_lazy("index")
  
  login_url = '/login'
  
  def form_valid(self, form):
    messages.success(self.request, "保存しました")
    return super().form_valid(form)

  def form_invalid(self, form):
    messages.error(self.request, "保存できませんでした")
    return super().form_invalid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
  model = Blog
  form_class = BlogForm
  template_name = 'blog/blog_update_form.html'
  # fields = ["content",]
  
  login_url = '/login'
  
  def form_valid(self, form):
    messages.success(self.request, "更新できました")
    return super().form_valid(form)
  
  def form_invalid(self, form):
    messages.error(self.request, "更新できませんでした")
    return super().form_invalid(form)
  
  def get_success_url(self):
    blog_id = self.kwargs['pk']
    url = reverse_lazy("detail", kwargs={"pk": blog_id})
    return url
  
class BlogDeleteView(LoginRequiredMixin, DeleteView):
  model = Blog
  success_url = reverse_lazy("index")
  
  login_url = '/login'
  
  def delete(self, request, *args, **kwargs):
    messages.success(self.request, "削除しました")
    return super().delete(request, *args, **kwargs)
  
  

