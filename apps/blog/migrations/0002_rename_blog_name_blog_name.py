# Generated by Django 5.0.1 on 2024-01-28 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_name',
            new_name='name',
        ),
    ]
