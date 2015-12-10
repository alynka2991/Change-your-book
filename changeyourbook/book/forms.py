
from django.forms import ModelForm
from models import Comments
from models import Book
class CommentForm(ModelForm):
	class Meta:
		model=Comments
		fields = ['comments_text']

class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = ['book_title', 'book_author', 'book_genre', 'book_publisher', 'book_year']