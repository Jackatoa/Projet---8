from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserCreateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Compte enregistré pour {username} ! Vous pouvez '
            f'maintenant vous connecter.')
            return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
