from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='details_post'),
    path('post/create/', views.PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='edit_post'),
]