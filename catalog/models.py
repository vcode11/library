#-*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
import uuid # Required for uniqure book instances

class Genre(models.Model):
    """ Model for representing a book genre """
    name = models.CharField(max_length=200, help_text='Enter a book genre Ex: Fiction')

    def __str__(self):
        """ String representation of genre model """
        return self.name

class Author(models.Model):
    """ Model representing an Author """
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        """ Returns url for particular author instance. """
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the model object."""
        return f'{self.last_name}, {self.first_name}'
class Book(models.Model):
    """ Model representing a book but not a specific copy of book. """
    title = models.CharField(max_length=200)
    #To Do many to many relationship in authors and books
    author  = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=500, 
                               help_text="Enter a brief description", 
                               null=True, blank= True,)
    isbn = models.CharField('ISBN', 
                            max_length=13, 
                            help_text='13 Character <a href="https://www.isbn-'
                                      'international.org/content/what-isbn">ISBN number</a>',
                            null=True, blank=True)
    genre = models.ManyToManyField(Genre, help_text='Choose a genre for this book.')

    def __str__(self):
        """ String representation of model book """
        return self.title

    def get_absolute_url(self):
        """ URL for a book """
        pass
        #return reverse('book-detail', args=[str(self.id)])
class BookInstance(models.Model):
     """ Model representing a specific copy of book that can be borrowed """
     id = models.UUIDField(primary_key=True, 
                           default=uuid.uuid4,
                           help_text='Unique id across whole library for this book.')
     book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
     due_back = models.DateField(null=True, blank=True,)

     LOAN_STATUS = (
         ('m', 'Maintenance'),
         ('o', 'On Loan'),
         ('a', 'Available'),
         ('r', 'Reserved'),
         ('l', 'Lost'),
     )
     status = models.CharField(
         max_length = 1,
         choices = LOAN_STATUS,
         blank=True,
         default='m',
         help_text='Book Availability',
     )
     class Meta:
         ordering =['due_back']
    
     def __str__(self):
        """ String representation for the model object. """
        return f'{self.id} {self.book.title}'


    