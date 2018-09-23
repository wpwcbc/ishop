from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .form import Signupform
from ishopapp.models import Phone
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            user = form.save()
            ContactNo = form.cleaned_data['ContactNo']
            phone = Phone.objects.create(ContactNo=ContactNo, user=user)
            # log the user in
            auth_login(request, user)
            return redirect('ishop:index')
    else:
        form = Signupform()
    return render(request,'signup.html', {'form':form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            auth_login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('ishop:index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})


def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('ishop:index')