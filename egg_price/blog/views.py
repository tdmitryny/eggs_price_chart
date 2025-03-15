from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.filter(published_date__isnull=False).order_by('-published_date')
    paginator = Paginator(posts, 3)  # Show 3 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/blog_detail.html', {'post': post})
