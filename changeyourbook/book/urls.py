from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^1/', 'book.views.basic_one'),
    url(r'^2/', 'book.views.template_two'),
    url(r'^3/', 'book.views.template_three_simple'),
    url(r'^books/all/$', 'book.views.books'),
    url(r'^books/alll/$','book.views.bookss'),
    url(r'^books/get/(?P<book_id>\d+)/$', 'book.views.book'),
    url(r'^books/addlike/(?P<book_id>\d+)/$', 'book.views.addlike'),
    url(r'^books/addcomment/(?P<book_id>\d+)/$', 'book.views.addcomment'),
    url(r'books/add/$','book.views.addbook'),
    url(r'^books/delete_book/(?P<book_id>\d+)/$','book.views.delete'),
    url(r'^books/deletecomment/(?P<comment_id>\d+)/$','book.views.delete_com'),
    url(r'^books/add_photo/$','book.views.add_photo'),
    url(r'^search_form/byauthor/$', 'book.views.search_form_byauthor'),
    url(r'^search_form/bytitle/$', 'book.views.search_form_bytitle'),
    url(r'^search_form/bygenre/$', 'book.views.search_form_bygenre'),
    url(r'^search_form/byuser/$', 'book.views.search_form_byuser'),
    url(r'^search/byauthor/$', 'book.views.search_byauthor'),
    url(r'^search/bytitle/$', 'book.views.search_bytitle'),
    url(r'^search/bygenre/$', 'book.views.search_bygenre'),
    url(r'^search/byuser/$', 'book.views.search_byuser'),
    url(r'^', 'book.views.main'),
    ]
