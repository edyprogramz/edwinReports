# Generated by Django 5.0.2 on 2024-03-03 22:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='privacypolicy',
            name='ppolicy',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]