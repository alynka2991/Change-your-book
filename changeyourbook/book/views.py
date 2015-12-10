

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.shortcuts import render_to_response, redirect, render
from book.models import Book, Comments
from django.core.exceptions import ObjectDoesNotExist
from forms import CommentForm, BookForm
from django.core.context_processors import csrf
from django.contrib import auth
from django.utils import timezone
from django.shortcuts import get_object_or_404


# Create your views here.
def basic_one(request):
	view = "basic_one"
	html="<html><body>This is %s view</html></body>" % view
	return HttpResponse(html)

def template_two(request):
	view = "template_two"
	t = get_template('book.html')
	html = t.render({'name':view})
	return HttpResponse(html)

def template_three_simple(request):
	view = "template_three"
	return render_to_response('Myview.html',{'name': view})

def books(request):
	#return render_to_response('index2.html')
	return render_to_response('news_registrate_user.html',{'books': Book.objects.all(),'username':auth.get_user(request).username})

def book(request, book_id):
	comment_form = CommentForm
	args={}
	args.update(csrf(request))
	args['book'] = Book.objects.get(id=book_id)
	args['comments']=Comments.objects.filter(comments_book_id=book_id)
	args['form']=comment_form
	args['username'] = auth.get_user(request).username
	return render_to_response('book.html',args)

def addlike(request, book_id):
	try:
		if book_id in request.COOKIES:
			redirect('/')
		else:
			book = Book.objects.get(id = book_id)
			book.book_likes += 1
			book.save()
			response = redirect('/')
			response.set_cookie(book_id, "test")
			return response
	except ObjectDoesNotExist:
		raise Http404
	return redirect('/')

def addcomment(request,book_id):
	if request.POST and ("pause" not in request.session):
		form=CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.comments_book=Book.objects.get(id=book_id)
			comment.comments_from=request.user
			comment.comments_date=timezone.now()
			form.save()
			request.session.set_expiry(60)
			request.session['pause'] = True
	return redirect('/books/get/%s/'%book_id)

def main(request):
	return render_to_response('first.html',{'username':auth.get_user(request).username})

def bookss(request):
	return render_to_response('books1.html',{'books': Book.objects.all(),'username':auth.get_user(request).username})

def addbook(request):
	args={}
	args.update(csrf(request))
	args['form']=BookForm()
	args['username'] = auth.get_user(request).username
	if request.POST:
		form=BookForm(request.POST, request.FILES)
		if form.is_valid():
			book = form.save(commit=False)
			book.book_from = request.user
			book.book_date = timezone.now()
			book.save()
			return redirect('/books/get/%s/' %book.id)
	else:
		form=BookForm()
	return render_to_response('AddBook.html', args)

def delete(request, book_id):
	args={}
	args.update(csrf(request))
	args['username'] = auth.get_user(request).username
	if request.POST:
		book = get_object_or_404(Book, id=book_id)
		book.delete()
		return redirect('/books/all/')
	return render_to_response('book.html', args)

def delete_com(request,comment_id):
	args={}
	args.update(csrf(request))
	if request.POST:
		comment = get_object_or_404(Comments, id=comment_id)
		comment.delete()
		return redirect ('book.html',args)
	return render_to_response('book.html', args)

def add_photo(request):
	if request.method=='POST':
		form=UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['file'])
			return HttpResponseRedirect('/')
	else:
		form=UploadFileForm()
	return render_to_response('AddBook,html', {'form':form})

def search_bytitle(request):
	if 'q' in request.GET and request.GET['q']:
		q=request.GET['q']
		books=Book.objects.filter(book_title__icontains=q)
		return render(request, 'search_simple_bytitle.html',{'books': books, 'query': q, })
	else:
		return HttpResponse('Please submit a search term.')

def search_byauthor(request):
	if 'q' in request.GET and request.GET['q']:
		q=request.GET['q']
		books=Book.objects.filter(book_author__icontains=q)
		return render(request, 'search_simple_byauthor.html',{'books': books, 'query': q, })
	else:
		return HttpResponse('Please submit a search term.')

def search_bygenre(request):
	if 'q' in request.GET and request.GET['q']:
		q=request.GET['q']
		books=Book.objects.filter(book_genre__icontains=q)
		return render(request, 'search_simple_bygenre.html',{'books': books, 'query': q, })
	else:
		return HttpResponse('Please submit a search term.')

#def search_byuser(request):
	#if 'q' in request.GET and request.GET['q']:
		#q=request.GET['q']
		#books=Book.objects.filter(book_from=q)
		#return render(request, 'search_simple_byuser.html',{'books': books, 'query': q, })
	#else:
		#return HttpResponse('Please submit a search term.')

def search_form_byauthor(request):
    return render(request, 'search_simple_byauthor.html')

def search_form_bytitle(request):
    return render(request, 'search_simple_bytitle.html')

def search_form_bygenre(request):
    return render(request, 'search_simple_bygenre.html')

#def search_form_byuser(request):
    #return render(request, 'search_simple_byuser.html')



