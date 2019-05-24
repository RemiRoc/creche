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
	LundiDepos		= forms.ChoiceField(label='A quelle heure souhaitez vous déposer votre enfant le Lundi ? ', choices=DebutFrequentationLundi)
	LundiRepris		= forms.ChoiceField(label='A quelle heure souhaitez vous récupérer votre enfant le Lundi ? ', choices=FinFrequentationLundi)
	MardiDepos		= forms.ChoiceField(label='A quelle heure souhaitez vous déposer votre enfant le Mardi ? ', choices=DebutFrequentationMardi)
	MardiRepris		= forms.ChoiceField(label='A quelle heure souhaitez vous récupérer votre enfant le Mardi ? ', choices=FinFrequentationMardi)
	MercrediDepos	= forms.ChoiceField(label='A quelle heure souhaitez vous déposer votre enfant le Mercredi ? ', choices=DebutFrequentationMercredi)
	MercrediRepris	= forms.ChoiceField(label='A quelle heure souhaitez vous récupérer votre enfant le Mercredi ? ', choices=FinFrequentationMercredi)
	JeudiDepos		= forms.ChoiceField(label='A quelle heure souhaitez vous déposer votre enfant le Jeudi ? ', choices=DebutFrequentationJeudi)
	JeudiRepris		= forms.ChoiceField(label='A quelle heure souhaitez vous récupérer votre enfant le Jeudi ? ', choices=FinFrequentationJeudi)
	VendrediDepos	= forms.ChoiceField(label='A quelle heure souhaitez vous déposer votre enfant le Vendredi ? ', choices=DebutFrequentationVendredi)
	VendrediRepris	= forms.ChoiceField(label='A quelle heure souhaitez vous récupérer votre enfant le Vendredi ? ', choices=FinFrequentationVendredi)


	nomAssurrance			= forms.CharField(label='Nom de l\'assurance de l\'enfant  ', validators=[validate_carac],max_length=30)
	certificatMedical 		= forms.FileField(label='Certificat médical de l\'enfant  ')
	AssuranceCivile			= forms.FileField(label='Assurance civile de l\'enfant  ')
	protocoleDeTemperature 	= forms.FileField(label='Protocole de température  ')
	AutorisationMedicament 	= forms.FileField(label='Autorisation de distribution de medicament ')
	FichePoliceAssurance	= forms.FileField(label='Fiche sur laquelle se situe la police d\'assurance  ')	


	def process(self):
		clean = self.cleaned_data