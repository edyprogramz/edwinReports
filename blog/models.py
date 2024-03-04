from django.db import models
from ckeditor.fields import RichTextField 

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField('title', max_length=100)
    category = models.ForeignKey(BlogCategory, related_name="blogs", on_delete=models.CASCADE)
    section1 = RichTextField() 
    section2 = RichTextField(null=True, blank=True) 
    section3 = RichTextField(null=True, blank=True) 
    section4 = RichTextField(null=True, blank=True) 
    upload_date = models.DateTimeField(auto_now_add=True)  # Add default value for upload_date
    ad = models.TextField(null=True, blank=True)
    ad_box = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)


    def __str__(self):
        return self.title
    

