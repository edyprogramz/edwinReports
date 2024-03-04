from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.
class AboutMe(models.Model):
    about = RichTextField(null=True, blank=True) 
    
    def __str__(self):
        return self.about
    
class PrivacyPolicy(models.Model):
    ppolicy = RichTextField(null=True, blank=True) 
    
    def __str__(self):
        return self.ppolicy
