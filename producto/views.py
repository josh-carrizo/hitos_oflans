from django.shortcuts import render, redirect
from .models import Flan
from .forms import ContactFormModelForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False) 
    context = {
        'flanes': flanes_publicos
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        'flanes': flanes_privados,
        'user': request.user
    }
    return render(request, 'welcome.html', context)

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactFormModelForm()
    return render(request, 'contacto.html', {'form': form})

def success(request):
    return render(request, 'success.html', {'message': 'Gracias por contactarte con OnlyFlans, te responderemos en breve.'})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
