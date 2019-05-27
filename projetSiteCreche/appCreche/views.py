
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import CustomUserCreationForm, InscriptionEnfant, deposFacture
from .models import Parent, Enfant, CustomUser, EnfantPreinscrit

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
		form = InscriptionEnfant(request.POST, request.FILES)
		
		if form.is_valid():
			user = CustomUser()
			user = request.user
			enfant = Enfant()
			parent = Parent()
			preinscrit = EnfantPreinscrit()
			enfant.nom 				 		= request.POST.get("nomEnfant")
			enfant.prenom 			 		= request.POST.get("prenomEnfant")
			enfant.dateDeNaissance   		= request.POST.get("dateDeNaissance")
			enfant.arriveLundi 		 		= request.POST.get("LundiDepos")
			enfant.partLundi 		 		= request.POST.get("LundiRepris")
			enfant.arriveMardi 		 		= request.POST.get("MardiDepos")
			enfant.partMardi		 		= request.POST.get("MardiRepris")
			enfant.arriveMercredi    		= request.POST.get("MercrediDepos")
			enfant.partMercredi	     		= request.POST.get("MercrediRepris")
			enfant.arriveJeudi 		 		= request.POST.get("JeudiDepos")
			enfant.partJeudi 				= request.POST.get("JeudiRepris")
			enfant.arriveVendredi    		= request.POST.get("VendrediDepos")
			enfant.partVendredi 			= request.POST.get("VendrediRepris")
			enfant.NomDocteur				= request.POST.get("NomDocteur")
			enfant.telDocteur				= request.POST.get("numTelDocteur")
			enfant.nomAssurance				= request.POST.get("nomAssurance")

			enfant.certificatMedical 		= request.FILES["certificatMedical"]
			enfant.AssuranceCivile			= request.FILES["AssuranceCivile"]
			enfant.protocoleDeTemperature	= request.FILES["protocoleDeTemperature"]
			enfant.AutorisationMedicament	= request.FILES["AutorisationMedicament"]
			enfant.FichePoliceAssurance		= request.FILES["FichePoliceAssurance"]
			

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
			user.is_Parent				 = True
			



			if(Enfant.objects.filter(nom = enfant.nom, prenom = enfant.prenom, dateDeNaissance = enfant.dateDeNaissance).first() is None or Parent.objects.filter(parentUser = request.user).first() is None):
				if(Parent.objects.filter(parentUser = request.user).first() is None):
					parent.save()
					enfant.Parents = parent
					enfant.save()	
					preinscrit.Enfant = enfant
					preinscrit.save()
					user.save()
					return render(request, 'AppCreche/InscrireEnfant.html')
				else:
					enfant.Parents = Parent.objects.filter(parentUser = request.user).first()
					enfant.save()
					preinscrit.Enfant = enfant
					preinscrit.save()
					user.save()
					return render(request, 'AppCreche/InscrireEnfant.html')
					

	else:
		form = InscriptionEnfant()

	return render(request, 'appCreche/inscriptionEnfant.html',{'form':form})

def deposFactures(request):
	if request.method == 'POST':
		form = deposFacture(request.POST, request.FILES)
		
		if form.is_valid():
			parent = Parent()
			if(Parent.objects.filter(prenom_Pere = request.POST.get("prenomPere"), nom_Pere = request.POST.get("nomPere"), prenom_Mere = request.POST.get("prenomMere"), nom_Mere = request.POST.get("nomMere")).first()):
				parent = Parent.objects.filter(prenom_Pere = request.POST.get("prenomPere"), nom_Pere = request.POST.get("nomPere"), prenom_Mere = request.POST.get("prenomMere"), nom_Mere = request.POST.get("nomMere")).first()
				parent.FactureCreche = request.FILES["Facture"]
				parent.save()
				return render(request, 'appCreche/factureDeposee.html')
	else:
		form = deposFacture()

	return render(request, 'appCreche/deposFacture.html',{'form':form})			

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

