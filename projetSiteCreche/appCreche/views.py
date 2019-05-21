
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, EnfantCreationForm
from .models import Parent, Enfant
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

def inscriptionEnfant(request):

	enfant = Enfant()
	parent = Parent()
	print('soleil')
	if(	(enfant == Enfant.objects.filter(nom =  request.POST.get("nomEnfant"), prenom =  request.POST.get("prenomEnfant")).first() is None ) and (parent == Parent.objects.filter(parentUser = request.user).first() is None)):
		print('lune')

		enfant.nom 				= request.POST.get("nomEnfant")
		enfant.prenom 			= request.POST.get("prenomEnfant")
		enfant.dateDeNaissance  = request.POST.get("dateDeNaissance")
		enfant.arriveLundi 		= request.POST.get("FrequentationLundiDepos")
		enfant.partLundi 		= request.POST.get("FrequentationLundiRepris")
		enfant.arriveMardi 		= request.POST.get("FrequentationMardiDepos")
		enfant.partMardi		= request.POST.get("FrequentationMardiRepris")
		enfant.arriveMercredi   = request.POST.get("FrequentationMercrediDepos")
		enfant.partMercredi	    = request.POST.get("FrequentationMercrediRepris")
		enfant.arriveJeudi 		= request.POST.get("FrequentationJeudiDepos")
		enfant.partJeudi 		= request.POST.get("FrequentationJeudiRepris")
		enfant.arriveVendredi   = request.POST.get("FrequentationVendrediDepos")
		enfant.partVendredi 	= request.POST.get("FrequentationVendrediRepris")

		

		parent.nom_Mere				 = request.POST.get("nomMere")
		parent.prenom_Mere			 = request.POST.get("prenomMere")
		parent.adresseMail_Mere	 	 = request.POST.get("mailMere")
		parent.num_Mere			 	 = request.POST.get("telMere")
		parent.profession_Mere 		 = request.POST.get("ProfessionMere")
		parent.telEmployeur_Mere     = request.POST.get("telEmpMere")	
		parent.nom_Pere 			 = request.POST.get("nomPere")
		parent.prenom_Pere 			 = request.POST.get("prenomPere")
		parent.adresseMail_Pere	 	 = request.POST.get("mailPere")
		parent.num_Pere 			 = request.POST.get("telPere")
		parent.telEmployeur_Pere	 = request.POST.get("telEmpPere")
		parent.profession_Pere 	 	 = request.POST.get("ProfessionPere")
		parent.adresse 			 	 = request.POST.get("adresse")
		parent.secondeAdresse	 	 = request.POST.get("adresseDeux")
		parent.nbEnfantAuFoyer 		 = request.POST.get("nbEnfantFoyer")
		parent.parentUser			 = request.user
		prenom_Enfant 				 = request.POST.get("prenomEnfant")
		
		parent.save()
		enfant.save()
	

	return render(request, 'AppCreche/inscriptionEnfant.html')

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

