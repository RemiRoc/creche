import datetime
from django.contrib.auth.models import AbstractUser
from appCreche.horaires import *
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator
from django.contrib import admin
from django.db import models




class Parent(models.Model):
	
	nom				= models.CharField(_('nom'),max_length=20)
	prenom			= models.CharField(_('prenom'),max_length=20)
	adresseMail		= models.EmailField(_('email'), max_length=254)
	num				= models.DecimalField(_('telephone'), max_digits=10, decimal_places=0)
	telEmployeur	= models.DecimalField(_('telephone de l\'employeur'), max_digits=10, decimal_places=0)
	profession 		= models.CharField(_("profession"), max_length=64)
	adresse			= models.CharField(_("adresse"), max_length=256)
	secondeAdresse	= models.CharField(_("seconde adresse"), max_length=256, null=True)
	nbEnfantAuFoyer	= models.PositiveIntegerField(_("nb enfant au foyer"), validators=[MaxValueValidator(20)])

	class Meta:
		verbose_name = _('Parent')
		verbose_name_plural = _('Parents')

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

	def get_tel_employeur(self):
		return self.telEmployeur

	def get_profession(self):
		return self.profession

	def get_adresse(self):
		return self.adresse

	def get_seconde_adresse(self):
		return self.secondeAdresse or "Il n'y a pas de seconde adresse"

	def get_nb_enfant_au_foyer(self):
		return self.nbEnfantAuFoyer

class Enfant(models.Model):
	#INFO PERSO
	nom		= models.CharField(_('nom'),max_length=20)
	prenom	= models.CharField(_('prenom'),max_length=20)
	dateDeNaissance = models.DateField(_('Date de Naissance'))
	#WALLAH C'EST LA DOC QUI M'A DIT DE METTRE + A LA FIN
	parent1 = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name=_('Parent 1+'))
	parent2 = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name=_('Parent 2+'))
	
	#HORAIRES DU GAMIN
	#LUNDI
	arriveLundi		= models.CharField(max_length=3, choices=DebutFrequentationLundi, default='')
	partLundi		= models.CharField(max_length=4, choices=FinFrequentationLundi, default='')
	#MARDI
	arriveMardi		= models.CharField(max_length=3, choices=DebutFrequentationMardi, default='')
	partMardi		= models.CharField(max_length=4, choices=FinFrequentationMardi, default='')
	#MERCREDI
	arriveMercredi	= models.CharField(max_length=3, choices=DebutFrequentationMercredi, default='')
	partMercredi	= models.CharField(max_length=4, choices=FinFrequentationMercredi, default='')
	#JEUDI
	arriveJeudi		= models.CharField(max_length=3, choices=DebutFrequentationJeudi, default='')
	partJeudi		= models.CharField(max_length=4, choices=FinFrequentationJeudi, default='')
	#VENDREDI
	arriveVendredi	= models.CharField(max_length=3, choices=DebutFrequentationVendredi, default='')
	partVendredi	= models.CharField(max_length=4, choices=FinFrequentationVendredi, default='')

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
	def clean(self):
		direct	= Parent.objects.filter(person1 = self.person1, person2 = self.person2)
		reverse	= Parent.objects.filter(person1 = self.person2, person2 = self.person1) 

		if direct.exists() or reverse.exists():
			raise ValidationError(_('C\'est pas bien de mettre deux fois le même parent'))

class Contributeur(models.Model):
	nom			= models.CharField(_('nom'),max_length=20)
	prenom		= models.CharField(_('prenom'),max_length=20)
	adresseMail	= models.EmailField(_('email'), max_length=254)
	num			= models.DecimalField(_('telephone'), max_digits=10, decimal_places=0)

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
	nom			= models.CharField(_('nom'),max_length=20)
	prenom		= models.CharField(_('prenom'),max_length=20)
	adresseMail	= models.EmailField(_('email'), max_length=254)
	num			= models.DecimalField(_('telephone'), max_digits=10, decimal_places=0)
	#HORAIRES PERSONEL
	horaireSemaineJaune = models.CharField(_("Horaires semaine Jaune"), max_length=4, choices=semaineJaune, default='')
	horaireSemaineRouge = models.CharField(_("Horaires semaine Rouge"), max_length=4, choices=semaineRouge, default='')
	horaireSemaineBleue = models.CharField(_("Horaires semaine Bleue"), max_length=4, choices=semaineBleue, default='')
	horaireSemaineVerte = models.CharField(_("Horaires semaine Verte"), max_length=4, choices=semaineVerte, default='')
	horaireSemaineNoire = models.CharField(_("Horaires semaine Noire"), max_length=4, choices=semaineNoire, default='')
	horaireSemaineRose = models.CharField(_("Horaires semaine Rose"), max_length=4, choices=semaineRose, default='')

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

class CustomUser(AbstractUser):
    # add additional fields in here

    def __str__(self):
        return self.email