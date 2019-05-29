#templates/forms.py
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Enfant, Parent
import datetime
from django.utils import timezone
from .horaires import *
from .validateurs import *

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email','is_Parent', 'is_Employe')

class InscriptionEnfant(forms.Form):

	prenomEnfant 	= forms.CharField(label='Prenom de votre Enfant', max_length=20, validators=[validate_carac])
	nomEnfant 		= forms.CharField(label='Nom de votre Enfant', max_length=30, validators=[validate_carac])
	dateDeNaissance = forms.DateField(label='Date de naissance de votre Enfant',  widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
	NomDocteur		= forms.CharField(label='Nom du médecin traitant de l\'enfant',max_length=20, validators=[validate_carac])
	numTelDocteur	= forms.CharField(label='Numéro de téléphone du médecin traitant', min_length=10, max_length=10, validators=[validate_tel])


	prenomMere 		= forms.CharField(label='Prénom de la Mère', max_length=20, validators=[validate_carac])
	nomMere		 	= forms.CharField(label='Nom de la Mère', max_length=30, validators=[validate_carac])
	telMere 		= forms.CharField(label='Numéro de téléphone de la Mère', min_length=10, max_length=10, validators=[validate_tel])
	mailMere 		= forms.EmailField(label='Email de la Mère')
	ProfessionMere  = forms.CharField(label='Profession de la Mère', max_length=30, validators=[validate_carac])
	telEmpMere 		= forms.CharField(label='Numéro de l\'employeur de la mère', min_length=10, max_length=10, validators=[validate_tel])
	

	prenomPere 		= forms.CharField(label='Prénom du Père', max_length=20, validators=[validate_carac])
	nomPere 		= forms.CharField(label='Nom du Père', max_length=30, validators=[validate_carac])
	telPere 		= forms.CharField(label='Numéro de téléphone du Père', min_length=10, max_length=10, validators=[validate_tel])
	mailPere 		= forms.EmailField(label='Email du Père')
	ProfessionPere  = forms.CharField(label='Profession du Père', max_length=30, validators=[validate_carac])
	telEmpPere 		= forms.CharField(label='Numéro de l\'employeur du Père', min_length=10, max_length=10, validators=[validate_tel])


	adresse 		= forms.CharField(label='Saisissez l\'adresse de résidence de l\'Enfant', max_length=256, validators=[validate_adresse])
	ville			= forms.CharField(label='Ville de résidence de l\'Enfant ', max_length=50, validators=[validate_carac])
	adresseDeux		= forms.CharField(label='Saisissez la deuxieme adresse de résidence de l\'enfant ( si il y en a une )', max_length=256,validators=[validate_adresse], required=False)
	villeDeux		= forms.CharField(label='Seconde ville de résidence de l\'Enfant ', max_length=50, validators=[validate_carac], required=False)
	nbEnfantFoyer	= forms.IntegerField(label='Nombre d\'enfant au Foyer')
	LundiDepos		= forms.ChoiceField(label='A quelle heure souhaitez vous déposer votre enfant le Lundi ? ', choices=DebutFrequentation)
	LundiRepris		= forms.ChoiceField(label='A quelle heure souhaitez vous récupérer votre enfant le Lundi ? ', choices=FinFrequentation)
	MardiDepos		= forms.ChoiceField(label='A quelle heure souhaitez vous déposer votre enfant le Mardi ? ', choices=DebutFrequentation)
	MardiRepris		= forms.ChoiceField(label='A quelle heure souhaitez vous récupérer votre enfant le Mardi ? ', choices=FinFrequentation)
	MercrediDepos	= forms.ChoiceField(label='A quelle heure souhaitez vous déposer votre enfant le Mercredi ? ', choices=DebutFrequentation)
	MercrediRepris	= forms.ChoiceField(label='A quelle heure souhaitez vous récupérer votre enfant le Mercredi ? ', choices=FinFrequentation)
	JeudiDepos		= forms.ChoiceField(label='A quelle heure souhaitez vous déposer votre enfant le Jeudi ? ', choices=DebutFrequentation)
	JeudiRepris		= forms.ChoiceField(label='A quelle heure souhaitez vous récupérer votre enfant le Jeudi ? ', choices=FinFrequentation)
	VendrediDepos	= forms.ChoiceField(label='A quelle heure souhaitez vous déposer votre enfant le Vendredi ? ', choices=DebutFrequentation)
	VendrediRepris	= forms.ChoiceField(label='A quelle heure souhaitez vous récupérer votre enfant le Vendredi ? ', choices=FinFrequentation)


	nomAssurance			= forms.CharField(label='Nom de l\'assurance de l\'enfant  ', validators=[validate_carac],max_length=30)
	certificatMedical 		= forms.FileField(label='Certificat médical de l\'enfant  ')
	AssuranceCivile			= forms.FileField(label='Assurance civile de l\'enfant  ')
	protocoleDeTemperature 	= forms.FileField(label='Protocole de température  ')
	AutorisationMedicament 	= forms.FileField(label='Autorisation de distribution de medicament ')
	FichePoliceAssurance	= forms.FileField(label='Fiche sur laquelle se situe la police d\'assurance  ')	


	def process(self):
		clean = self.cleaned_data

class deposFacture(forms.Form):
	prenomPere 		= forms.CharField(label='Prénom du Père', max_length=20, validators=[validate_carac])
	prenomMere 		= forms.CharField(label='Prénom de la Mère', max_length=20, validators=[validate_carac])
	nomMere		 	= forms.CharField(label='Nom de la Mère', max_length=30, validators=[validate_carac])
	nomPere 		= forms.CharField(label='Nom du Père', max_length=30, validators=[validate_carac])
	Facture 		= forms.FileField(label='Dépos de Facture ')

	def process(self):
		clean = self.cleaned_data


class nouvelEmploye(forms.Form):

	nom 		= forms.CharField(label='Nom de L\'employé', max_length=20, validators=[validate_carac])
	prenom  	= forms.CharField(label='Prenom de L\'employé', max_length=20, validators=[validate_carac])
	adresseMail = forms.EmailField(label='Email de l\'employé')
	num 		= forms.CharField(label='Numéro de téléphone de l\'employé',min_length=10, max_length=10, validators=[validate_tel])

	horaireLundiSemaineJaune = forms.ChoiceField(label="Horaires du Lundi en semaine Jaune", choices=horaireEmpl)
	horaireMardiSemaineJaune = forms.ChoiceField(label="Horaires du Mardi en semaine Jaune", choices=horaireEmpl)
	horaireMercrediSemaineJaune = forms.ChoiceField(label="Horaires du Mercredi en semaine Jaune", choices=horaireEmpl)
	horaireJeudiSemaineJaune = forms.ChoiceField(label="Horaires du Jeudi en semaine Jaune", choices=horaireEmpl)
	horaireVendrediSemaineJaune = forms.ChoiceField(label="Horaires du Vendredi en semaine Jaune", choices=horaireEmpl)

	horaireLundiSemaineRouge = forms.ChoiceField(label="Horaires du Lundi en semaine Rouge", choices=horaireEmpl)
	horaireMardiSemaineRouge = forms.ChoiceField(label="Horaires du Mardi en semaine Rouge", choices=horaireEmpl)
	horaireMercrediSemaineRouge = forms.ChoiceField(label="Horaires du Mercredi en semaine Rouge", choices=horaireEmpl)
	horaireJeudiSemaineRouge = forms.ChoiceField(label="Horaires du Jeudi en semaine Rouge", choices=horaireEmpl)
	horaireVendrediSemaineRouge = forms.ChoiceField(label="Horaires du Vendredi en semaine Rouge", choices=horaireEmpl)
	
	horaireLundiSemaineBleue = forms.ChoiceField(label="Horaires du Lundi en semaine Bleue", choices=horaireEmpl)
	horaireMardiSemaineBleue = forms.ChoiceField(label="Horaires du Mardi en semaine Bleue", choices=horaireEmpl)
	horaireMercrediSemaineBleue = forms.ChoiceField(label="Horaires du Mercredi en semaine Bleue", choices=horaireEmpl)
	horaireJeudiSemaineBleue = forms.ChoiceField(label="Horaires du Jeudi en semaine Bleue", choices=horaireEmpl)
	horaireVendrediSemaineBleue = forms.ChoiceField(label="Horaires du Vendredi en semaine Bleue", choices=horaireEmpl)

	horaireLundiSemaineVerte = forms.ChoiceField(label="Horaires du Lundi en semaine Verte", choices=horaireEmpl)
	horaireMardiSemaineVerte = forms.ChoiceField(label="Horaires du Mardi en semaine Verte", choices=horaireEmpl)
	horaireMercrediSemaineVerte = forms.ChoiceField(label="Horaires du Mercredi en semaine Verte", choices=horaireEmpl)
	horaireJeudiSemaineVerte = forms.ChoiceField(label="Horaires du Jeudi en semaine Verte", choices=horaireEmpl)
	horaireVendrediSemaineVerte = forms.ChoiceField(label="Horaires du Vendredi en semaine Verte", choices=horaireEmpl)

	horaireLundiSemaineNoire = forms.ChoiceField(label="Horaires du Lundi en semaine Noire", choices=horaireEmpl)
	horaireMardiSemaineNoire = forms.ChoiceField(label="Horaires du Mardi en semaine Noire", choices=horaireEmpl)
	horaireMercrediSemaineNoire = forms.ChoiceField(label="Horaires du Mercredi en semaine Noire", choices=horaireEmpl)
	horaireJeudiSemaineNoire = forms.ChoiceField(label="Horaires du Jeudi en semaine Noire", choices=horaireEmpl)
	horaireVendrediSemaineNoire = forms.ChoiceField(label="Horaires du Vendredi en semaine Noire", choices=horaireEmpl)

	horaireLundiSemaineRose = forms.ChoiceField(label="Horaires du Lundi en semaine Rose", choices=horaireEmpl)
	horaireMardiSemaineRose = forms.ChoiceField(label="Horaires du Mardi en semaine Rose", choices=horaireEmpl)
	horaireMercrediSemaineRose = forms.ChoiceField(label="Horaires du Mercredi en semaine Rose", choices=horaireEmpl)
	horaireJeudiSemaineRose = forms.ChoiceField(label="Horaires du Jeudi en semaine Rose", choices=horaireEmpl)
	horaireVendrediSemaineRose = forms.ChoiceField(label="Horaires du Vendredi en semaine Rose", choices=horaireEmpl)

	def process(self):
		clean = self.cleaned_data