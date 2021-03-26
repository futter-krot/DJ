from django.contrib import admin
from p_library.models import Book,Author,Publisher

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_full_name',)
    fields = ('ISBN', 'title',  'author', 'year_release', 'publisher', 'description', 'price')

    '''@staticmethod
    def author_full_name(obj):
        return obj.author.full_name
    author_full_name.short_description = 'author' 
    '''



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'country')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass