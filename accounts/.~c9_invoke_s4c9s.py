from django.shortcuts import render, redirect, reverse
from django.contrib import messages, auth
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def get_index(request):
    return render(request, 'index.html')
    
# Create your views here.
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(get_index)
    
def login(request):
    if request.method=="POST":
        form=UserLoginForm(request.POST)
        
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])

            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in")
                return redirect(next)
            else:
                form.add_error(None, "Your username or password was not recognised")
            
    else:
        form = UserLoginForm()
    
    return render(request, "login.html", {'form': form})

def register(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password1'])
                                     
            if user is not None:
                auth.login(request, user)
                return redirect(get_index)
    else:
        form = UserRegistrationForm()
    
    return render(request, "register.html", {'form': form})
    
    
@login_required(login_url='/accounts/login')
def profile(request):
    return render(request, 'profile.html')    