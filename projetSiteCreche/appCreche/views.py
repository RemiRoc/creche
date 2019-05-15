
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
	return render(request, 'appCreche/base.html')
	
def equipe(request):
	return render(request, 'appCreche/equipe.html')

def contribuer(request):
	return render(request, 'appCreche/contribuer.html')

def recrutement(request):
	return render(request, 'appCreche/recrutement.html')

def inscription(request):
	return render(request, 'appCreche/inscription.html')

def inscriptionEnfant(request):
	return render(request, 'appCreche/inscriptionEnfant.html')

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


