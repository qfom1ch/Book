# Generated by Django 4.1.4 on 2023-01-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_book_is_best_selling'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
    ]