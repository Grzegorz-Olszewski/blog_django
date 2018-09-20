from django.views.generic.edit import ModelFormMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from django.utils import timezone


class PostListView(ListView):
    '''Class representing list view. It is used for
    representing home page with all posts listed.'''
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    '''Class representing detail view. It is used
    in page where post is displayed with all details.'''
    model = Post
    template_name = 'blog/details.html'


class PostCreateView(CreateView):
    '''Class representing create view. It is used
    on page where one can fill the form to create new post.
    Thanks for following convention of naming form template we
    don't have to make template_name variable, because template
    for form follows convenion of name_of_model_form.html, post_form.html
    in this example.'''
    model = Post
    fields = ['title', 'content']


class PostEditView(UpdateView):
    '''Class representing update view. It is used on page where
    user can edit post by changing title or content.'''
    model = Post
    template_name_suffix = '_update_form'
    fields = ['title', 'content']
