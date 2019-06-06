import datetime
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from appCreche.horaires import *
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator
from django.contrib import admin
from django.db import models
from .validateurs import *
from .path import * 

class CustomUser(AbstractUser):
	# add additional fields in here
	def getMailUser(self):
		return self.email
	is_Parent = models.BooleanField(default=False)
	is_Employe = models.BooleanField(default=False)

	"""
	ici nous créons un utilisateur personnalisé , qui aura tous les champs d'un utilisateur de base de Django, 
	mais aura également un champ email
	is_Parent ( pour vérifier si l'utilisateur a inscrit un enfant ) 
	is_Employe ( pour vérifier si l'utilisateur est un employe de la crèche )
	"""


class Parent(models.Model):
	#INFO PARENTS
	#parentUser permet de lier l'utilisateur au parent.		
	parentUser			= models.ForeignKey( CustomUser ,on_delete=models.CASCADE, null=True)
	nom_Mere			= models.CharField(_('Nom de la Mère'),max_length=20,validators=[validate_carac], null=True)
	prenom_Mere			= models.CharField(_('Prénom de la Mère'),max_length=20,validators=[validate_carac], null=True)
	adresseMail_Mere 	= models.EmailField(_('Email de la Mère'), null=True)
	num_Mere			= models.CharField(_('télephone de la Mère'), max_length=10, validators=[validate_tel], null=True)
	profession_Mere 	= models.CharField(_("Profession de la Mère"), validators=[validate_carac] , max_length=64, null=True)
	telEmployeur_Mere	= models.CharField(_('telephone de l\'employeur de la Mère'), max_length=10, validators=[validate_tel], null=True)
	nom_Pere			= models.CharField(_('Nom du Père'),max_length=20, validators=[validate_carac], null=True)
	prenom_Pere			= models.CharField(_('Prénom du Père'),max_length=20, validators=[validate_carac], null=True)
	adresseMail_Pere 	= models.EmailField(_('Email du Père'), null=True)	
	num_Pere			= models.CharField(_('télephone du Père'), max_length=10, validators=[validate_tel], null=True)	
	telEmployeur_Pere	= models.CharField(_('telephone de l\'employeur du Père'), max_length=10,  validators=[validate_tel], null=True)	
	profession_Pere 	= models.CharField(_("Profession du Père"), validators=[validate_carac], max_length=64, null=True)
	adresse				= models.CharField(_("Adresse"), validators=[validate_adresse], max_length=256, null=True)
	ville				= models.CharField(_("Ville"),validators=[validate_carac], max_length=50, null=True)
	secondeAdresse		= models.CharField(_("Seconde Adresse"),validators=[validate_adresse], max_length=256, blank=True, null=True)
	villeDeux			= models.CharField(_("Seconde Ville"),validators=[validate_carac], max_length=50,blank=True, null=True)
	nbEnfantAuFoyer		= models.CharField(_("Nombre d'enfant au foyer"), validators=[validate_nombre], max_length=1, null=True)
	FactureCreche		= models.FileField(_("Dernière Facture : "), upload_to=UploadToPathAndRename(os.path.join('Factures')), validators=[validate_file_size],blank=True, null=True)
	
	def __str__(self):
		full_name = '%s %s' % (self.nom_Mere, self.prenom_Mere)
		return full_name.strip()


	class Meta:
		verbose_name = _('Parent')
		verbose_name_plural = _('Parents')

#GETTERS
	def get_Parent(self):
		return Parent

	def get_parentUser(self):
		return self.parentUser

	def get_nomMere(self):
		return self.nom_Mere

	def get_prenomMere(self):
		return self.prenom_Mere

	def get_adresse_mail_Mere(self):
		return self.adresseMail_Mere

	def get_num_Mere(self):
		return self.num_Mere

	def get_tel_employeur_Mere(self):
		return self.telEmployeur_Mere

	def get_profession_Mere(self):
		return self.profession_Mere
	def get_nom_Pere(self):
		return self.nom_Pere

	def get_prenom_Pere(self):
		return self.prenom_Pere

	def get_adresse_mail_Pere(self):
		return self.adresseMail_Pere

	def get_num_Pere(self):
		return self.num_Pere

	def get_tel_employeur_Pere(self):
		return self.telEmployeur_Pere

	def get_profession_Pere(self):
		return self.profession_Pere

	def get_adresse(self):
		return self.adresse

	def get_seconde_adresse(self):
		return self.secondeAdresse or "Il n'y a pas de seconde adresse"

	def get_nb_enfant_au_foyer(self):
		return self.nbEnfantAuFoyer

class Enfant(models.Model):
	#INFO ENFANT
	nom						= models.CharField(_('nom'),max_length=20, validators=[validate_carac], null=True)
	prenom					= models.CharField(_('prenom'),max_length=20, validators=[validate_carac], null=True)
	dateDeNaissance 		= models.DateField(_('Date de Naissance'), null=True)
	Parents					= models.ForeignKey(Parent, on_delete=models.CASCADE, null=True)
	certificatMedical 		= models.FileField(_('Certificat Médical de l\'enfant '), validators=[validate_file_size],upload_to=UploadToPathAndRename(os.path.join( 'CertificatMedical')))
	AssuranceCivile			= models.FileField(_('Assurance Civile de l\'enfant '), validators=[validate_file_size],upload_to=UploadToPathAndRename(os.path.join('AssuranceCivile')))
	protocoleDeTemperature 	= models.FileField(_('Protocolde de température de l\'enfant '), validators=[validate_file_size],upload_to=UploadToPathAndRename(os.path.join('Protocole temp')))
	AutorisationMedicament 	= models.FileField(_('Autorisation de distribution de médicament de l\'enfant '), validators=[validate_file_size],upload_to=UploadToPathAndRename(os.path.join('Autorisation Medicament')))
	FichePoliceAssurance	= models.FileField(_('Police d\'assurance de l\'enfant '), validators=[validate_file_size],upload_to=UploadToPathAndRename(os.path.join('Police Assurance')))
	NomDocteur				= models.CharField(_('Nom du Médecin traitant'),max_length=20, validators=[validate_carac], null=True)
	telDocteur				= models.CharField(_('télephone du Médecin traitant'), max_length=10, validators=[validate_tel], null=True)
	nomAssurance			= models.CharField(_('Nom de la compagnie d\'assurance'),max_length=20, validators=[validate_carac], null=True)
	
	#HORAIRES DE L'ENFANT
	#LUNDI
	arriveLundi		= models.CharField(max_length=4, choices=DebutFrequentation, default='', null=True)
	partLundi		= models.CharField(max_length=5, choices=FinFrequentation, default='', null=True)
	#MARDI
	arriveMardi		= models.CharField(max_length=4, choices=DebutFrequentation, default='', null=True)
	partMardi		= models.CharField(max_length=5, choices=FinFrequentation, default='', null=True)
	#MERCREDI
	arriveMercredi	= models.CharField(max_length=4, choices=DebutFrequentation, default='', null=True)
	partMercredi	= models.CharField(max_length=5, choices=FinFrequentation, default='', null=True)
	#JEUDI
	arriveJeudi		= models.CharField(max_length=4, choices=DebutFrequentation, default='', null=True)
	partJeudi		= models.CharField(max_length=5, choices=FinFrequentation, default='', null=True)
	#VENDREDI
	arriveVendredi	= models.CharField(max_length=4, choices=DebutFrequentation, default='', null=True)
	partVendredi	= models.CharField(max_length=5, choices=FinFrequentation, default='', null=True)


	def __str__(self):
		full_name = '%s %s' % (self.nom, self.prenom)
		return full_name.strip()

	#GETTERS
	
	def get_nom(self):
		return self.nom 
		
	def get_prenom(self):
		return self.prenom

	def get_date_de_naissance(self):
		return self.dateDeNaissance
	
	def get_a_lundi(self):
		return self.arriveLundi

	def get_p_lundi(self):
		return self.partLundi

	def get_a_mardi(self):
		return self.arriveMardi

	def get_p_mardi(self):
		return self.partMardi
	
	def get_a_mercredi(self):
		return self.arriveMercredi
	
	def get_p_mercredi(self):
		return self.partMercredi

	def get_a_jeudi(self):
		return self.arriveJeudi

	def get_p_jeudi(self):
		return self.partJeudi

	def get_a_vendredi(self):
		return self.arriveVendredi

	def get_p_vendredi(self):
		return self.PartVendredi


	
class Employe(models.Model):
	#INFO PERSONEL
	nom					= models.CharField(_('nom'),max_length=20, validators=[validate_carac], null=True )
	prenom				= models.CharField(_('prenom'),max_length=20, validators=[validate_carac],null=True)
	adresseMail			= models.EmailField(_('Email de l\'employe'), null=True)
	num					= models.CharField(_('telephone'), max_length=10, validators=[validate_tel])
	empUser				= models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name=_('Utilisateur+'), null=True)
	#HORAIRES PERSONEL
	horaireLundiSemaineJaune = models.CharField(_("Horaires du Lundi en semaine Jaune"), max_length=25, choices=horaireEmpl, default='')
	horaireMardiSemaineJaune = models.CharField(_("Horaires du Mardi en semaine Jaune"), max_length=25, choices=horaireEmpl, default='')
	horaireMercrediSemaineJaune = models.CharField(_("Horaires du Mercredi en semaine Jaune"), max_length=25, choices=horaireEmpl, default='')
	horaireJeudiSemaineJaune = models.CharField(_("Horaires du Jeudi en semaine Jaune"), max_length=25, choices=horaireEmpl, default='')
	horaireVendrediSemaineJaune = models.CharField(_("Horaires du Vendredi en semaine Jaune"), max_length=25, choices=horaireEmpl, default='')

	horaireLundiSemaineRouge = models.CharField(_("Horaires du Lundi en semaine Rouge"), max_length=25, choices=horaireEmpl, default='')
	horaireMardiSemaineRouge = models.CharField(_("Horaires du Mardi en semaine Rouge"), max_length=25, choices=horaireEmpl, default='')
	horaireMercrediSemaineRouge = models.CharField(_("Horaires du Mercredi en semaine Rouge"), max_length=25, choices=horaireEmpl, default='')
	horaireJeudiSemaineRouge = models.CharField(_("Horaires du Jeudi en semaine Rouge"), max_length=25, choices=horaireEmpl, default='')
	horaireVendrediSemaineRouge = models.CharField(_("Horaires du Vendredi en semaine Rouge"), max_length=25, choices=horaireEmpl, default='')
	
	horaireLundiSemaineBleue = models.CharField(_("Horaires du Lundi en semaine Bleue"), max_length=25, choices=horaireEmpl, default='')
	horaireMardiSemaineBleue = models.CharField(_("Horaires du Mardi en semaine Bleue"), max_length=25, choices=horaireEmpl, default='')
	horaireMercrediSemaineBleue = models.CharField(_("Horaires du Mercredi en semaine Bleue"), max_length=25, choices=horaireEmpl, default='')
	horaireJeudiSemaineBleue = models.CharField(_("Horaires du Jeudi en semaine Bleue"), max_length=25, choices=horaireEmpl, default='')
	horaireVendrediSemaineBleue = models.CharField(_("Horaires du Vendredi en semaine Bleue"), max_length=25, choices=horaireEmpl, default='')

	horaireLundiSemaineVerte = models.CharField(_("Horaires du Lundi en semaine Verte"), max_length=25, choices=horaireEmpl, default='')
	horaireMardiSemaineVerte = models.CharField(_("Horaires du Mardi en semaine Verte"), max_length=25, choices=horaireEmpl, default='')
	horaireMercrediSemaineVerte = models.CharField(_("Horaires du Mercredi en semaine Verte"), max_length=25, choices=horaireEmpl, default='')
	horaireJeudiSemaineVerte = models.CharField(_("Horaires du Jeudi en semaine Verte"), max_length=25, choices=horaireEmpl, default='')
	horaireVendrediSemaineVerte = models.CharField(_("Horaires du Vendredi en semaine Verte"), max_length=25, choices=horaireEmpl, default='')

	horaireLundiSemaineNoire = models.CharField(_("Horaires du Lundi en semaine Noire"), max_length=25, choices=horaireEmpl, default='')
	horaireMardiSemaineNoire = models.CharField(_("Horaires du Mardi en semaine Noire"), max_length=25, choices=horaireEmpl, default='')
	horaireMercrediSemaineNoire = models.CharField(_("Horaires du Mercredi en semaine Noire"), max_length=25, choices=horaireEmpl, default='')
	horaireJeudiSemaineNoire = models.CharField(_("Horaires du Jeudi en semaine Noire"), max_length=25, choices=horaireEmpl, default='')
	horaireVendrediSemaineNoire = models.CharField(_("Horaires du Vendredi en semaine Noire"), max_length=25, choices=horaireEmpl, default='')

	horaireLundiSemaineRose = models.CharField(_("Horaires du Lundi en semaine Rose"), max_length=25, choices=horaireEmpl, default='')
	horaireMardiSemaineRose = models.CharField(_("Horaires du Mardi en semaine Rose"), max_length=25, choices=horaireEmpl, default='')
	horaireMercrediSemaineRose = models.CharField(_("Horaires du Mercredi en semaine Rose"), max_length=25, choices=horaireEmpl, default='')
	horaireJeudiSemaineRose = models.CharField(_("Horaires du Jeudi en semaine Rose"), max_length=25, choices=horaireEmpl, default='')
	horaireVendrediSemaineRose = models.CharField(_("Horaires du Vendredi en semaine Rose"), max_length=25, choices=horaireEmpl, default='')

	def __str__(self):
		full_name = '%s %s' % (self.nom, self.prenom)
		return full_name.strip()

	#GETTERS
	def get_nom(self):
		return self.nom

	def get_prenom(self):
		return self.prenom

	def get_adresse_mail(self):
		return self.adresseMail

	def get_num(self):
		return self.num

	def get_hs_jaune(self):
		return self.horaireSemaineJaune

	def get_hs_rouge(self):
		return self.horaireSemaineRouge

	def get_hs_bleue(self):
		return self.horaireSemaineBleue

	def get_hs_verte(self):
		return self.horaireSemaineVerte

	def get_hs_noire(self):
		return self.horaireSemaineNoire

	def get_hs_rose(self):
		return self.horaireSemaineRose


class OffreEmploi(models.Model):
	# Informations requises pour la création d'une offre sur le Site.
	
	intituleDuPoste = models.CharField(verbose_name="Intitulé du poste", max_length=100, default='')
	DescriptionDuPoste = models.TextField(verbose_name="Décrivez le poste", default='')
	diplomesRequis = models.CharField(verbose_name="Saisissez quels dîplômes sont requis pour ce poste", max_length=100, default='')
	Contact = models.EmailField(default='asso.gros.calin@gmail.com')

	#L'email par default est asso.gros.calin@gmail.com mais peut etre modifié lors de la création d'une offre.


"""
Les trois classes suivantes sont faites pour différencier les enfants entre eux :
Preinscrit : Le parent viens de remplir le Formulaire, la directrice doit examiner les informations et contacter le parent
En Attente : Le parent a eu un RDV téléphonique avec la Directrice de la creche, et elle a supprimé l'enfant du champ préinscrit et l'a placé en Attente.
Present : Ce sont les enfants qui sont inscrit a la crèche et qui s'y rendent. 
"""

class EnfantPreinscrit(models.Model):

	Enfant = models.ForeignKey(Enfant, on_delete=models.CASCADE, null=True)

class EnfantEnAttente(models.Model):

	Enfant = models.ForeignKey(Enfant, on_delete=models.CASCADE, null=True)

class EnfantPresent(models.Model):

	Enfant = models.ForeignKey(Enfant, on_delete=models.CASCADE, null=True)

