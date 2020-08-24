from django.views.generic import ListView, DetailView
from .forms import PostForm
from .models import Post
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
 
class BlogListView(ListView):
    context_object_name = 'articles'
    template_name = 'home.html'
    model = Post

    def get_queryset(self):
        articles = Post.objects.all()
        # Отбираем первые 10 статей
        paginator = Paginator(articles, 10)
        page = self.request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            articles = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            articles = paginator.page(paginator.num_pages)
        return articles



    
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

  
