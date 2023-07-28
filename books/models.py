from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

# class User(models.Model):
# first_name = models.CharField(max_length=200)
# last_name = models.CharField(max_length=200)
# email = models.EmailField(unique=True)
# phone_number = models.CharField(max_length=11)
# password = models.CharField(max_length=23)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11)


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    GENRE_CHOICES = [
        ('FICTION', 'Fiction'),
        ('FINANCE', 'Finance'),
        ('POLITICS', 'Politics'),
        ('ROMANCE', 'Romance')
    ]
    title = models.CharField(max_length=250, blank=False)
    isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=8, choices=GENRE_CHOICES, default="Finance")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_published = models.DateField(blank=True, null=True)
    copies = models.IntegerField()

    def __str__(self):
        # return self.title
        return f"{self.title} {self.isbn}"

    class Meta:
        ordering = ['-title']


class Address(models.Model):
    house_number = models.PositiveIntegerField()
    street_name = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=25, default="Nigeria")


class BookInstance(models.Model):
    book = models.OneToOneField(Book, on_delete=models.PROTECT, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_borrowed = models.DateField(auto_now_add=True)
    date_returned = models.DateField()
