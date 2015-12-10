#-*-coding:utf-8-*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	class Meta():
		db_table = "book"
	
	book_title = models.CharField(max_length = 200, verbose_name="Название")
	book_date = models.DateTimeField(blank = True, null = True)
	book_from = models.ForeignKey(User)
	book_author = models.CharField(max_length=100, blank = True, null = True, verbose_name="Автор")
	book_year = models.CharField(max_length=4, blank = True, null = True, verbose_name="Год издания")
	book_publisher = models.CharField(max_length=50, blank = True, null = True, verbose_name="Издательство")
	book_genre = models.CharField(max_length=50, blank = True, null = True, verbose_name="Жанр")
	book_image = models.FileField(blank = True, null = True)

class Comments(models.Model):
	class Meta():
		db_table = "comments"
	comments_date = models.DateTimeField()
	comments_text = models.TextField(verbose_name="Текст комментария")
	comments_book = models.ForeignKey(Book)
	comments_from = models.ForeignKey(User)

		
