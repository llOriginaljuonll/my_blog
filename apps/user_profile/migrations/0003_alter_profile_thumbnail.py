# Generated by Django 5.0.1 on 2024-05-25 14:55

import versatileimagefield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_profile_birth_date_alter_profile_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='thumbnail',
            field=versatileimagefield.fields.VersatileImageField(null=True, upload_to='images', verbose_name='Image'),
        ),
    ]
