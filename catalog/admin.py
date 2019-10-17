#-*- coding: utf-8 -*-
from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Shelf


def BulkSave(modelAdmin, request, queryset):
    """ Admin action to initialize copies of books. """
    for book_model in queryset:
        number = book_model.number_of_copies
        book_model.initialized=True
        book_model.save()
        for i in range(number):
                BookInstance.objects.create(shelf=book_model.book_shelf, book=book_model)
BulkSave.short_description = 'Initialize All Copies'

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
    list_display = ('title', 'display_author', 'display_genre','initialized' ,'isbn')
    list_filter = ('genre','author')
    actions=(BulkSave,)
    filter_horizontal = ('author', 'genre' )
    search_fields = ('title', 'isbn', 'author__first_name', 'author__last_name')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    search_fields = ('book', 'id')
