# Generated by Django 5.0.2 on 2024-02-27 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_pageview'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PageView',
        ),
    ]
