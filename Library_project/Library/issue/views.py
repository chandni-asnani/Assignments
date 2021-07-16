from django.shortcuts import render
from issue.models import Book, UserIssuing
from django.views.generic import View
from registration.views import User
from datetime import datetime


# Create your views here.
class Dashboard(View):

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        book_list = UserIssuing.objects.filter(user=user)


        return render(request, 'index.html', {"username":user.username, 'book':book_list})
    
    

class BookView(View):

    def get(self, request):
        # import code; code.interact(local=dict(globals(), **locals()))
        user_login = User.objects.get(id=request.user.id)
        issue = UserIssuing.objects.filter(user=user_login)
        books_id = []
        for issue_obj in issue:
            books_id.append(issue_obj.book.id)
        books = Book.objects.exclude(id__in=books_id)
        return render(request, 'list.html', {'book': books})

    def post(self,request):
        print(request.POST)
        user = User.objects.get(id=request.user.id)
        book = Book.objects.get(id=int(request.POST['books']))
        date = datetime.today()
        UserIssuing.objects.create(user=user,book=book,date=date)
        book_list = UserIssuing.objects.filter(user=user)
        #import code; code.interact(local=dict(globals(), **locals()))
        return render(request, 'index.html',{'username':user.username, 'book':book_list})
    
        



        



        
        


            

