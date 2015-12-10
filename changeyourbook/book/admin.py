from django.contrib import admin
from book.models import Book, Comments
# Register your models here.
class BookInLine(admin.StackedInline):
	model = Comments
	extra=2

class BookAdmin(admin.ModelAdmin):
	fields = ('book_title','book_author','book_date', 'book_year', 'book_publisher', 'book_genre', 'book_from')
	inlines = [BookInLine]
	list_filter = ['book_date']

admin.site.register(Book,BookAdmin)