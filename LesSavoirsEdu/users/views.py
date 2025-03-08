from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import CustomUser, Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "pages/index.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get("next")
            return redirect("home")
        else:
            messages.error(request, "Invalid Username or password")
            print('invalid details')
            return redirect('login')
    else:
        return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')
  

def signup_view(request):
    if request.method == "POST":
        email = request.POST.get("email")  
        first_name = request.POST.get("first_name")  
        last_name = request.POST.get("last_name") 
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        date_of_birth = request.POST.get("date_of_birth")
        

        
        user = CustomUser.objects.create_user(username=email, 
                                              password=password,
                                              email=email,
                                              first_name=first_name,
                                              last_name=last_name, 
                                              phone=phone,
                                              #date_of_birth=date_of_birth
                                              )
        Profile.objects.create(user=user)
     
        login(request, user)
        return redirect('home') 

    return render(request, 'accounts/signup.html')

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        profile = Profile.objects.filter(user=user).first()
        print(request.FILES.get('profile_image'))
        profile.profile_picture = request.FILES.get('profile_image')
        profile.save()
        return redirect('profile')
    user = request.user
    return render(request, 'accounts/profile.html', {'user': user})     