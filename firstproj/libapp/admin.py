from django.contrib import admin
from libapp.models import Book, PublicationHouse, Review

class ReviewInline(admin.TabularInline):
  model = Review
  extra = 1

class BookAdmin(admin.ModelAdmin):
  list_display = ['title', 'pages', 'price']
  fields = ['title', 'price', 'pages', 'publicationhouse']
  search_fields = ['title']
  list_filter = ['pages', 'price']
  inlines = [ReviewInline]

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(PublicationHouse)
