from django.db import models

# Create your models here.

class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)
    def __str__(self):
        return self.full_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True, blank=True)

    def author_full_name(self):
        return self.author.full_name
    author_full_name.short_description = 'author name'

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.TextField()
    full_name = models.TextField()

    def __str__(self):
        return self.name
