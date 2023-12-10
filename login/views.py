

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
def home(request):
    return render(request,'home.html')

@login_required
def Cursos(request):
    if request.user.is_authenticated:
        return render(request, 'Cursos.html')
    else:
        return redirect('login')

def exit(request):
    logout(request)
    return redirect('home')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Usuario no encontrado. Por favor, verifica tus credenciales.')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})