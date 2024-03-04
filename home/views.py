from django.shortcuts import render
from blog.models import Blog, BlogCategory
from home.models import AboutMe, PrivacyPolicy

# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    categories = BlogCategory.objects.all()        

    return render(request, "home.html", {
        'blogs':blogs,
        "categories":categories,
    })

def about(request):
    about = AboutMe.objects.first()
    ppolicy = PrivacyPolicy.objects.first()

    return render(request, "about.html", {
        'about':about,
        "ppolicy":ppolicy
    })