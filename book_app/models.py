from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Book(models.Model):
    title = models.CharField(max_length=70)
    title2 = models.CharField(max_length=70)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField()
    author = models.CharField(max_length=100,null=True)
    slug = models.SlugField(default='', null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title2)
        super(Book, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('one_books_url', args=[self.slug])

    def __str__(self):
        return f'Назнание - {self.title}, Рейтинг - {self.rating}, Бестселлер - {self.is_best_selling}, Автор - {self.author}'

