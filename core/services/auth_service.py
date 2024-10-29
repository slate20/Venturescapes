from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from core.forms import CustomUserCreationForm
from core.models import Player, Business
from django.shortcuts import render, redirect

class AuthService:
    @staticmethod
    def register(request):
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()

                # Login the user
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
                login(request, user)

                # Create a Player instance tied to the user
                Player.objects.get_or_create(user=request.user)

                # Redirect to the player setup
                return redirect('biz_setup')
        else:
            form = CustomUserCreationForm()

        return render(request, 'register.html', {'form': form})
    
    @staticmethod
    def login_user(request):
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('main_layout')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
    @staticmethod
    def logout_user(request):
        logout(request)
        return redirect('login')