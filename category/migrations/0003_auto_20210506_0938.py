# Generated by Django 3.1 on 2021-05-06 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20210503_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(blank=True, upload_to='photo/categories'),
        ),
    ]
