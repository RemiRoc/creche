from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import CustomUserCreationForm, InscriptionEnfant, deposFacture, nouvelEmploye
from .models import *

# Create your views here.
def index(request):
	return render(request, 'appCreche/base.html')
	
def recrutement(request):
	offres = {
	'OffreEmploi': OffreEmploi.objects.all(),
	}
	return render(request, 'appCreche/recrutement.html', offres)

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



def projetPedagogique(request):
	return render(request, 'appCreche/projetPedagogique.html')



def inscritEmploye(request):

	if request.method == 'POST':
		form = nouvelEmploye(request.POST)
		
		if form.is_valid():

			emp = Employe()

			emp.nom 							= request.POST.get("nom")
			emp.prenom 							= request.POST.get("prenom")
			emp.num 							= request.POST.get("num")
			emp.adresseMail 					= request.POST.get("adresseMail")
			emp.horaireLundiSemaineJaune		= request.POST.get("horaireLundiSemaineJaune")
			emp.horaireMardiSemaineJaune		= request.POST.get("horaireMardiSemaineJaune")
			emp.horaireMercrediSemaineJaune		= request.POST.get("horaireMercrediSemaineJaune")
			emp.horaireJeudiSemaineJaune		= request.POST.get("horaireJeudiSemaineJaune")
			emp.horaireVendrediSemaineJaune		= request.POST.get("horaireVendrediSemaineJaune")
			emp.horaireLundiSemaineRouge		= request.POST.get("horaireLundiSemaineRouge")
			emp.horaireMardiSemaineRouge		= request.POST.get("horaireMardiSemaineRouge") 
			emp.horaireMercrediSemaineRouge		= request.POST.get("horaireMercrediSemaineRouge")
			emp.horaireJeudiSemaineRouge		= request.POST.get("horaireJeudiSemaineRouge")
			emp.horaireVendrediSemaineRouge		= request.POST.get("horaireVendrediSemaineRouge")
			emp.horaireLundiSemaineBleue		= request.POST.get("horaireLundiSemaineBleue") 
			emp.horaireMardiSemaineBleue		= request.POST.get("horaireMardiSemaineBleue")
			emp.horaireMercrediSemaineBleue		= request.POST.get("horaireMercrediSemaineBleue") 
			emp.horaireJeudiSemaineBleue		= request.POST.get("horaireJeudiSemaineBleue")
			emp.horaireVendrediSemaineBleue		= request.POST.get("horaireVendrediSemaineBleue")
			emp.horaireLundiSemaineVerte		= request.POST.get("horaireLundiSemaineVerte")
			emp.horaireMardiSemaineVerte		= request.POST.get("horaireMardiSemaineVerte")
			emp.horaireMercrediSemaineVerte		= request.POST.get("horaireMercrediSemaineVerte")
			emp.horaireJeudiSemaineVerte		= request.POST.get("horaireJeudiSemaineVerte")
			emp.horaireVendrediSemaineVerte		= request.POST.get("horaireVendrediSemaineVerte")
			emp.horaireLundiSemaineNoire		= request.POST.get("horaireLundiSemaineNoire")
			emp.horaireMardiSemaineNoire		= request.POST.get("horaireMardiSemaineNoire")
			emp.horaireMercrediSemaineNoire		= request.POST.get("horaireMercrediSemaineNoire")
			emp.horaireJeudiSemaineNoire		= request.POST.get("horaireJeudiSemaineNoire")
			emp.horaireVendrediSemaineNoire		= request.POST.get("horaireVendrediSemaineNoire")
			emp.horaireLundiSemaineRose			= request.POST.get("horaireLundiSemaineRose")
			emp.horaireMardiSemaineRose			= request.POST.get("horaireMardiSemaineRose")
			emp.horaireMercrediSemaineRose		= request.POST.get("horaireMercrediSemaineRose")
			emp.horaireJeudiSemaineRose			= request.POST.get("horaireJeudiSemaineRose")
			emp.horaireVendrediSemaineRose		= request.POST.get("horaireVendrediSemaineRose")
			user = CustomUser.objects.filter(email = emp.adresseMail).first()
			emp.empUser = user
			
			if(Employe.objects.filter(nom = emp.nom, prenom = emp.prenom).first() is None or Employe.objects.filter(adresseMail = emp.adresseMail).first() is None or Employe.objects.filter(empUser = emp.empUser).first() is None):
				
				emp.save()
				user.is_Employe	= True
				user.save()
				return render(request, 'appCreche/employeInscrit.html')

	else:
		form = nouvelEmploye()

	return render(request, 'appCreche/inscritEmploye.html',{'form':form})



def monCompte(request):

	context = {
		'parent': Parent.objects.filter(parentUser = request.user).first(),
		'enfant': Enfant.objects.filter(Parents = Parent.objects.filter(parentUser = request.user).first()).first(),
		'employe': Employe.objects.filter(empUser = request.user).first(),
		'EnfantPreinscrit': EnfantPreinscrit.objects.filter(Enfant = Enfant.objects.filter(Parents = Parent.objects.filter(parentUser = request.user).first()).first()).first(),
		'EnfantEnAttente': EnfantEnAttente.objects.filter(Enfant = Enfant.objects.filter(Parents = Parent.objects.filter(parentUser = request.user).first()).first()).first(),
		'EnfantPresent': EnfantPresent.objects.filter(Enfant = Enfant.objects.filter(Parents = Parent.objects.filter(parentUser = request.user).first()).first()).first(),
		'nbEnfant': EnfantPresent.objects.count(),
		'placeSoirLundi': EnfantPresent.objects.filter(Enfant__in = Enfant.objects.exclude(partLundi = "16h30")).count(),
		'placeSoirMardi': EnfantPresent.objects.filter(Enfant__in = Enfant.objects.exclude(partMardi = "16h30")).count(),
		'placeSoirMercredi': EnfantPresent.objects.filter(Enfant__in = Enfant.objects.exclude(partMercredi = "16h30")).count(),
		'placeSoirJeudi': EnfantPresent.objects.filter(Enfant__in = Enfant.objects.exclude(partJeudi = "16h30")).count(),
		'placeSoirVendredi': EnfantPresent.objects.filter(Enfant__in = Enfant.objects.exclude(partVendredi = "16h30")).count(),
		


	}
	return render(request, 'appCreche/monCompte.html', context)

