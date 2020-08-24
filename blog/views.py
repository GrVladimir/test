from django.views.generic import ListView, DetailView
from .forms import PostForm
from .models import Post
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
 
 
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    
class BlogDetailView(DetailView): 
    model = Post
    template_name = 'post_detail.html'

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

  
