from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Player, Business


# Create your views here.
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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_layout')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def main_layout(request):
    return render(request, 'main_layout.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'hx_view': 'true'})

def biz_setup(request):
    player = Player.objects.get(user=request.user)

    # If the player already has an active business, redirect to the main layout
    if player.active_business_id:
        return redirect('main_layout')
    else:
        if request.method == 'POST':
            business_name = request.POST.get('business_name')
            business_type = request.POST.get('business_type')
            industry = request.POST.get('industry')

            # Create a Business instance that belongs to the player
            business = Business.objects.create(
                player_owner=player,
                business_name=business_name,
                business_type=business_type,
                industry=industry
            )

            # Set the business as the player's active business
            player.active_business_id = business
            player.save()

            return redirect('main_layout')
        else:
            return render(request, 'player_setup.html')