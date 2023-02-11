from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_book),
    path('book/<slug:slug_book>', views.one_book, name='one_books_url'),
]