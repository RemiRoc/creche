from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import CustomUserCreationForm, InscriptionEnfant, deposFacture, nouvelEmploye
from .models import *
from appCreche.token import account_activation_token
from appCreche.mail import sendConfirmationMail, createLink


# Create your views here.
def index(request):
	return render(request, 'appCreche/home.html')


	
def recrutement(request):
	offres = {
	'OffreEmploi': OffreEmploi.objects.all(),
	}
	return render(request, 'appCreche/recrutement.html', offres)

#Récupère toutes les offres d'emploi et les renvoies vers la page html



def inscription(request):
	"""Register view"""

	if request.user.is_authenticated:
		return  HttpResponseRedirect(reverse('home'))
	if not request.method == "POST":
		return render(request, 'signup.html', {'form': CustomUserCreationForm()})
	form = CustomUserCreationForm(request.POST)

	if not form.is_valid():
		return render(request, 'signup.html', {'form': form})

	
	to_email = form.cleaned_data.get('email')
	if(CustomUser.objects.filter(email= to_email).first() is None):
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = CustomUser(email=to_email, username=username, password=password)
		user.set_password(password)
		user.is_active = False
		user.save()
		user = CustomUser.objects.get(email=to_email)
		current_site = get_current_site(request)
		activation_link = createLink(user)
		activation_link = "http://{0}{1}".format(current_site, activation_link)
		message = render_to_string('register_email_template.html', {'link': activation_link, })
		email = sendConfirmationMail(message=message, to=[to_email])
		return HttpResponseRedirect(reverse('login'))
	else:
		return render(request, 'signup.html', {'form': form})
"""
Cette fonction permet de vérifier que l'utilisateur n'est pas connecté,
que le formulaire est bien en méthode POST 
et que l'utilisateur n'existe pas déjà. 
si ces trois conditions sont réunies, cela envoie un mail de validation a l'utilisateur.
"""

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


"""
Cette fonction réécupère toutes les entrées POST du formulaire d'inscription d'un enfant, vérifie s'il n'y a pas un enfant ayant le même nom et prenom et date de naissance
cela regarde aussi l'utilisateur, si c'est un nouvel utilisateur cela créé un nouveau parent et attribue la valeur True a is_Parent de l'utilisateur, 
sinon cela ajoute un enfant au parent possedant le champ parentUSer correspondant a l'utilisateur actuel. 
"""




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

"""
Formulaire permettant de déposer une facture pour un Parent donné.
"""

def projetPedagogique(request):
	return render(request, 'appCreche/projetPedagogique.html')

#retourne la page projet pedagogique.


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

#Cette fonction vérifie que l'utilisateur que l'on veut passer en Employé existe,
#Elle récupère ensuite toutes les entrées du formulaire et enregistre l'employe.
#Cela modifie également la valeur is_Employe de l'utilisateur, pour la passer en True

def monCompte(request):

	context = {
		'parent': Parent.objects.filter(parentUser = request.user).first(),
		'enfant': Enfant.objects.filter(Parents = Parent.objects.filter(parentUser = request.user).first()).first(),
		'employe': Employe.objects.filter(empUser = request.user).first(),
		'EnfantPreinscrit': EnfantPreinscrit.objects.filter(Enfant = Enfant.objects.filter(Parents = Parent.objects.filter(parentUser = request.user).first()).first()).first(),
		'EnfantEnAttente': EnfantEnAttente.objects.filter(Enfant = Enfant.objects.filter(Parents = Parent.objects.filter(parentUser = request.user).first()).first()).first(),
		'EnfantPresent': EnfantPresent.objects.filter(Enfant = Enfant.objects.filter(Parents = Parent.objects.filter(parentUser = request.user).first()).first()).first(),
		
		}
	return render(request, 'appCreche/monCompte.html', context)
"""
retourne vers la page MonCompte, en renvoyant les informations des parents et enfants ( en fonction des utilisateurs )
Renvoie également les employe.
"""

def activate(request, uid, token):
	"""Account activation view"""
	
	try:
		uid = urlsafe_base64_decode(uid).decode()
		#Décode l'uid qui se trouve dans l'url, l'uid correspondant a une adresse Mail
		user = CustomUser.objects.get(email=uid)
		#Vérifie que l'adresse Mail correspond a un utilisateur
		#si cela ne correpond pas , cela retourne une erreur et renvoie le message " Le lien d\'activation est invalide ! "
	except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
      # active l'utilisateur pour qu'il puisse se connecter:
		user.is_active = True

		user.save()
		return index(request)
	else:
		return HttpResponse('Le lien d\'activation est invalide ! ')

