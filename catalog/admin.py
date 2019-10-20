#-*- coding: utf-8 -*-
from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Shelf
from django.core.exceptions import ValidationError
from .forms import BookInstanceAdminForm
admin.site.register(Shelf)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_author', 'display_genre' ,'isbn')
    list_filter = ('genre','author')
    filter_horizontal = ('author', 'genre' )
    search_fields = ('title', 'isbn', 'author__first_name', 'author__last_name')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    form = BookInstanceAdminForm
    list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    search_fields = ('book', 'id')
