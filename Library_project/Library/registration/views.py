from django.shortcuts import render
from django.shortcuts import render,HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import UserForm
from issue.models import Book, UserIssuing



class SignUpView(View):

    def get(self,request):
        form = UserForm()
        return render(request, 'signup.html',{'form':form})



    def post(self,request):
        form = UserForm(request.POST)
        

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


class LoginView(View):

    def get(self,request):
        # import code; code.interact(local=dict(globals(), **locals()))
        user = User.objects.get(id=request.user.id)
        book_list = UserIssuing.objects.filter(user=user)
        if user.is_authenticated:
            return render(request, 'index.html', {"username": user.username, 'book':book_list})
        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form})
    
    def post(self,request):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            pswrd = form.cleaned_data['password']
            user = authenticate(username = name, password = pswrd)
            login(request,user)
            user = User.objects.get(id=request.user.id)
            book_list = UserIssuing.objects.filter(user=user)

            return render(request, 'index.html', {"username": user.username, 'book':book_list})
        else:
            form = AuthenticationForm()
            error = "Please use valid creds."
            return render(request, "login.html", {"form": form, "error": error})

class LogoutView(View):
    def get(self,request):
        logout(request)
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})






