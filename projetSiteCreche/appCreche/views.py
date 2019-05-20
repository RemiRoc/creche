
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, EnfantCreationForm

# Create your views here.
def index(request):
	return render(request, 'appCreche/base.html')
	
def equipe(request):
	return render(request, 'appCreche/equipe.html')

def contribuer(request):
	return render(request, 'appCreche/contribuer.html')

def recrutement(request):
	return render(request, 'appCreche/recrutement.html')

class inscription(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class inscriptionEnfant(generic.CreateView):
	form_class = EnfantCreationForm
	success_url = reverse_lazy('appCreche/home')
	template_name = 'AppCreche/inscriptionEnfant.html'

def connexion(request):
	return render(request, 'appCreche/connexion.html')

def deconnexion(request):
	return render(request, 'appCreche/deconnexion.html')

def petitesAnnonces(request):
	return render(request, 'appCreche/petitesAnnonces.html')

def modificationEnfantPonctuel(request):
	return render(request, 'appCreche/modificationEnfantPonctuel.html')

def tableauEmploye(request):
	return render(request, 'appCreche/tableauEmploye.html')

def monCompte(request):
	return render(request, 'appCreche/monCompte.html')

