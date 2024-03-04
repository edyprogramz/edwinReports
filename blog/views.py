from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Blog, BlogCategory
from django.db.models import Q

def index(request):
    blog = Blog.objects.last()
    blogs = Blog.objects.all()[:4]
    categories = BlogCategory.objects.all()
    
    return render(request, 'index.html', {
        "blog": blog,
        "blogs":blogs,
        "categories": categories
    })

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    blogs = Blog.objects.all()[:4]
    # category = blog.category.name
    categories = BlogCategory.objects.all()

    
    return render(request, "index.html", {
        "blog":blog,
        "blogs":blogs,
        "categories": categories
    })

def search(request):
    query = request.GET.get('q')
    results = Blog.objects.filter(Q(title__icontains=query) | Q(category__name__icontains=query))
    return render(request, 'index.html', {'results': results})



