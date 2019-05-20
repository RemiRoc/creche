import datetime
from django.contrib.auth.models import AbstractUser
from appCreche.horaires import *
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator
from django.contrib import admin
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
	def getMailUser(self):
		return self.email
	is_Parent = models.BooleanField(default=False)
	is_Employe = models.BooleanField(default=False)
	is_Contrib = models.BooleanField(default=False)
		
class Famille(models.Model):
	parentUser			= models.OneToOneField( CustomUser ,related_name="login+",on_delete=models.CASCADE, null=True)
	nom_Mere			= models.CharField(_('Nom de la Mère'),max_length=20)
	prenom_Mere			= models.CharField(_('Prénom de la Mère'),max_length=20)
	profession_Mere 	= models.CharField(_("Profession de la Mère"), max_length=64)
	adresseMail_Mere 	= models.EmailField(_('Email de la Mère'))
	num_Mere			= models.DecimalField(_('télephone de la Mère'), max_digits=10, decimal_places=0)
	telEmployeur_Mere	= models.DecimalField(_('telephone de l\'employeur de la Mère'), max_digits=10, decimal_places=0)
	nom_Pere			= models.CharField(_('Nom du Père'),max_length=20)
	prenom_Pere			= models.CharField(_('Prénom du Père'),max_length=20)
	adresseMail_Pere 	= models.EmailField(_('Email du Père'))	
	num_Pere			= models.DecimalField(_('télephone du Père'), max_digits=10, decimal_places=0)	
	telEmployeur_Pere	= models.DecimalField(_('telephone de l\'employeur du Père'), max_digits=10, decimal_places=0)	
	profession_Pere 	= models.CharField(_("Profession du Père"), max_length=64)
	adresse				= models.CharField(_("Adresse"), max_length=256)
	secondeAdresse		= models.CharField(_("Seconde Adresse"), max_length=256, blank=True)
	nbEnfantAuFoyer		= models.PositiveIntegerField(_("Nombre d'enfant au foyer"), validators=[MaxValueValidator(20)])
	

	class Meta:
		verbose_name = _('Famille')
		verbose_name_plural = _('Familles')

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


	#INFO PERSO
	nom_Enfant		= models.CharField(_('nom'),max_length=20)
	prenom_Enfant	= models.CharField(_('prenom'),max_length=20)
	dateDeNaissance_Enfant = models.DateField(_('Date de Naissance'))

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
"""
	#POUR EVITER LE BULLSHIT DU MEME PARENT
	def clean(self):
		direct	= Parent.objects.filter(person1 = self.person1, person2 = self.person2)
		reverse	= Parent.objects.filter(person1 = self.person2, person2 = self.person1) 

		if direct.exists() or reverse.exists():
			raise ValidationError(_('Une personne ne peux pas être doublement parent. Si ? '))
"""
class Contributeur(models.Model):
	nom			= models.CharField(_('nom'),max_length=20)
	prenom		= models.CharField(_('prenom'),max_length=20)
	adresseMail	= models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name=_('Utilisateur+'), null=True)
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
	adresseMail	= models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name=_('Utilisateur+'), null=True)
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


class OffreEmploi(models.Model):

	intituleDuPoste = models.CharField(verbose_name="Saisissez l'intitulé du poste", max_length=100, default='')
	DescriptionDuPoste = models.CharField(verbose_name="Décrivez le poste", max_length=999, default='')
	diplomesRequis = models.CharField(verbose_name="Saisissez quels dîplômes sont requis pour ce poste", max_length=100, default='')
	Contact = models.EmailField(default='asso.gros.calin@gmail.com')


class ListeDAttente(models.Model):

	Enfant = models.ForeignKey(Famille, on_delete=models.CASCADE, null=True)

class EnfantPresent(models.Model):

	Enfant = models.ForeignKey(Famille, on_delete=models.CASCADE, null=True)