from django.contrib import admin

from home.models import AboutMe, PrivacyPolicy

# Register your models here.
admin.site.register(AboutMe)
admin.site.register(PrivacyPolicy)
