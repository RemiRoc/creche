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
	is_Contrib = models.BooleanField(default=False)
		


class Parent(models.Model):

		
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
	nbEnfantAuFoyer		= models.PositiveIntegerField(_("Nombre d'enfant au foyer"), validators=[MaxValueValidator(20)], null=True)
	FactureCreche		= models.FileField(_("Dernière Facture : "), upload_to=UploadToPathAndRename(os.path.join('Factures')),blank=True, null=True)
	
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
	#INFO PERSO
	nom						= models.CharField(_('nom'),max_length=20, validators=[validate_carac], null=True)
	prenom					= models.CharField(_('prenom'),max_length=20, validators=[validate_carac], null=True)
	dateDeNaissance 		= models.DateField(_('Date de Naissance'), null=True)
	Parents					= models.ForeignKey(Parent, on_delete=models.CASCADE, null=True)
	certificatMedical 		= models.FileField(_('Certificat Médical de l\'enfant '),upload_to=UploadToPathAndRename(os.path.join( 'CertificatMedical')))
	AssuranceCivile			= models.FileField(_('Assurance Civile de l\'enfant '),upload_to=UploadToPathAndRename(os.path.join('AssuranceCivile')))
	protocoleDeTemperature 	= models.FileField(_('Protocolde de température de l\'enfant '),upload_to=UploadToPathAndRename(os.path.join('Protocole temp')))
	AutorisationMedicament 	= models.FileField(_('Autorisation de distribution de médicament de l\'enfant '),upload_to=UploadToPathAndRename(os.path.join('Autorisation Medicament')))
	FichePoliceAssurance	= models.FileField(_('Police d\'assurance de l\'enfant '),upload_to=UploadToPathAndRename(os.path.join('Police Assurance')))
	NomDocteur				= models.CharField(_('Nom du Médecin traitant'),max_length=20, validators=[validate_carac], null=True)
	telDocteur				= models.CharField(_('télephone du Médecin traitant'), max_length=10, validators=[validate_tel], null=True)
	nomAssurance			= models.CharField(_('Nom de la compagnie d\'assurance'),max_length=20, validators=[validate_carac], null=True)
	
	#HORAIRES DU GAMIN
	#LUNDI
	arriveLundi		= models.CharField(max_length=3, choices=DebutFrequentationLundi, default='', null=True)
	partLundi		= models.CharField(max_length=4, choices=FinFrequentationLundi, default='', null=True)
	#MARDI
	arriveMardi		= models.CharField(max_length=3, choices=DebutFrequentationMardi, default='', null=True)
	partMardi		= models.CharField(max_length=4, choices=FinFrequentationMardi, default='', null=True)
	#MERCREDI
	arriveMercredi	= models.CharField(max_length=3, choices=DebutFrequentationMercredi, default='', null=True)
	partMercredi	= models.CharField(max_length=4, choices=FinFrequentationMercredi, default='', null=True)
	#JEUDI
	arriveJeudi		= models.CharField(max_length=3, choices=DebutFrequentationJeudi, default='', null=True)
	partJeudi		= models.CharField(max_length=4, choices=FinFrequentationJeudi, default='', null=True)
	#VENDREDI
	arriveVendredi	= models.CharField(max_length=3, choices=DebutFrequentationVendredi, default='', null=True)
	partVendredi	= models.CharField(max_length=4, choices=FinFrequentationVendredi, default='', null=True)

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
	
	def get_parent1(self):
		p = Parent.objects.get(pk=self.parent1)
		return p
	
	def get_parent2(self):
		p = Parent.objects.get(pk=self.parent2)
		return p

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

	#POUR EVITER LE BULLSHIT DU MEME PARENT
	


class Contributeur(models.Model):
	nom			= models.CharField(_('nom'),max_length=20, validators=[validate_carac], null=True)
	prenom		= models.CharField(_('prenom'),max_length=20, validators=[validate_carac],null=True)
	adresseMail	= models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name=_('Utilisateur+'), null=True)
	num			= models.CharField(_('telephone'), max_length=10, validators=[validate_tel])

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

class Employe(models.Model):
	#INFO PERSONEL
	nom					= models.CharField(_('nom'),max_length=20, validators=[validate_carac], null=True )
	prenom				= models.CharField(_('prenom'),max_length=20, validators=[validate_carac],null=True)
	adresseMail			= models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name=_('Utilisateur+'), null=True)
	num					= models.CharField(_('telephone'), max_length=10, validators=[validate_tel])
	
	#HORAIRES PERSONEL
	horaireSemaineJaune = models.CharField(_("Horaires semaine Jaune"), max_length=4, choices=semaineJaune, default='')
	horaireSemaineRouge = models.CharField(_("Horaires semaine Rouge"), max_length=4, choices=semaineRouge, default='')
	horaireSemaineBleue = models.CharField(_("Horaires semaine Bleue"), max_length=4, choices=semaineBleue, default='')
	horaireSemaineVerte = models.CharField(_("Horaires semaine Verte"), max_length=4, choices=semaineVerte, default='')
	horaireSemaineNoire = models.CharField(_("Horaires semaine Noire"), max_length=4, choices=semaineNoire, default='')
	horaireSemaineRose 	= models.CharField(_("Horaires semaine Rose"), max_length=4, choices=semaineRose, default='')

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

	intituleDuPoste = models.CharField(verbose_name="Saisissez l'intitulé du poste", max_length=100, default='')
	DescriptionDuPoste = models.TextField(verbose_name="Décrivez le poste", default='')
	diplomesRequis = models.CharField(verbose_name="Saisissez quels dîplômes sont requis pour ce poste", max_length=100, default='')
	Contact = models.EmailField(default='asso.gros.calin@gmail.com')


class EnfantPreinscrit(models.Model):

	Enfant = models.ForeignKey(Enfant, on_delete=models.CASCADE, null=True)

class EnfantEnAttente(models.Model):

	Enfant = models.ForeignKey(Enfant, on_delete=models.CASCADE, null=True)

class EnfantPresent(models.Model):

	Enfant = models.ForeignKey(Enfant, on_delete=models.CASCADE, null=True)