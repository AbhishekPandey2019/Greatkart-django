# Generated by Django 3.1 on 2021-05-30 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_variation'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variation',
            field=models.ManyToManyField(blank=True, to='store.Variation'),
        ),
    ]
