from django.urls import path
from blog.views import index, blog_detail, search

app_name = 'blog'

urlpatterns = [
    path('', index, name="index"),
    path('blog/<int:pk>', blog_detail, name="blog_detail"),
    path('search/', search, name='search'),
]