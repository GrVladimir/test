from django.urls import path
from . import views
from .views import BlogListView, BlogDetailView 
 
urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), # новое изменение
    path('', BlogListView.as_view(), name='home'),
    path('post/new/', views.post_new, name='post_new')
]