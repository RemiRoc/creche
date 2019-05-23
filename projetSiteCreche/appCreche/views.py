
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import CustomUserCreationForm, InscriptionEnfant
from .models import Parent, Enfant, CustomUser, EnfantEnAttente
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
	if request.method == 'POST':
		form = InscriptionEnfant(request.POST)
		
		if form.is_valid():
			enfant = Enfant()
			parent = Parent()
			Attente = EnfantEnAttente()
			enfant.nom 				= request.POST.get("nomEnfant")
			enfant.prenom 			= request.POST.get("prenomEnfant")
			enfant.dateDeNaissance  = request.POST.get("dateDeNaissance")
			enfant.arriveLundi 		= request.POST.get("LundiDepos")
			enfant.partLundi 		= request.POST.get("LundiRepris")
			enfant.arriveMardi 		= request.POST.get("MardiDepos")
			enfant.partMardi		= request.POST.get("MardiRepris")
			enfant.arriveMercredi   = request.POST.get("MercrediDepos")
			enfant.partMercredi	    = request.POST.get("MercrediRepris")
			enfant.arriveJeudi 		= request.POST.get("JeudiDepos")
			enfant.partJeudi 		= request.POST.get("JeudiRepris")
			enfant.arriveVendredi   = request.POST.get("VendrediDepos")
			enfant.partVendredi 	= request.POST.get("VendrediRepris")

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
			parent.ville				 = request.POST.get("ville")
			parent.secondeAdresse	 	 = request.POST.get("adresseDeux")
			parent.villeDeux			 = request.POST.get("villeDeux")
			parent.nbEnfantAuFoyer 		 = request.POST.get("nbEnfantFoyer")
			parent.parentUser			 = request.user
			
			request.user.is_Parent		 = True
			
			if(Enfant.objects.filter(nom = enfant.nom, prenom = enfant.prenom).first() is None or Parent.objects.filter(parentUser = request.user).first() is None):
				if(Parent.objects.filter(parentUser = request.user).first() is None):
					parent.save()
					enfant.Parents = parent
					enfant.save()	
					Attente.Enfant = enfant
					Attente.save()
					return render(request, 'AppCreche/InscrireEnfant.html')
				else:
					enfant.Parents = Parent.objects.filter(parentUser = request.user).first()
					enfant.save()
					Attente.Enfant = enfant
					Attente.save()
					return render(request, 'AppCreche/InscrireEnfant.html')
					

	else:
		form = InscriptionEnfant()

	return render(request, 'appCreche/inscriptionEnfant.html',{'form':form})

def InscrireEnfant(request):
		
	
		return render(request, 'AppCreche/PasInscrireEnfant.html')


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

