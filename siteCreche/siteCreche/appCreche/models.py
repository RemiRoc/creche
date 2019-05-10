from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Enfant(models.Model):
#	id_Enfant = models.ForeignKey(Parent, on_delete=models.CASCADE)
	nom_Enfant = models.CharField(max_length=20, default='')
	Prenom_Enfant = models.CharField(max_length=20, default='')
	Date_De_Naissance = models.DateField('Date de Naissance',default='')
	DebutFrequentationLundi =(
		('no', 'Ne Viens pas'),
        ('730', '7h30'),
        ('800', '8h00'),
        ('830', '8h30'),
        ('900', '9h00'),
        ('930', '9h30'),
        )
	FinFrequentationLundi =(
		('no', 'Ne viens pas'),
		('1630', '16h30'),
		('1700', '17h00'),
		('1730', '17h30'),
		('1800', '18h00'),
		('1830', '18h30'),
		)
	DebutFrequentationMardi = (
		('no', 'Ne Viens pas'),
        ('730', '7h30'),
        ('800', '8h00'),
        ('830', '8h30'),
        ('900', '9h00'),
        ('930', '9h30'),
        )
	FinFrequentationMardi = (
		('no', 'Ne viens pas'),
		('1630', '16h30'),
		('1700', '17h00'),
		('1730', '17h30'),
		('1800', '18h00'),
		('1830', '18h30'),
		)
	DebutFrequentationMercredi =  (
		('no', 'Ne Viens pas'),
        ('730', '7h30'),
        ('800', '8h00'),
        ('830', '8h30'),
        ('900', '9h00'),
        ('930', '9h30'),
        )
	FinFrequentationMercredi = (
		('no', 'Ne viens pas'),
		('1630', '16h30'),
		('1700', '17h00'),
		('1730', '17h30'),
		('1800', '18h00'),
		('1830', '18h30'),
		)
	DebutFrequentationJeudi = (
		('no', 'Ne Viens pas'),
        ('730', '7h30'),
        ('800', '8h00'),
        ('830', '8h30'),
        ('900', '9h00'),
        ('930', '9h30'),
        )
	FinFrequentationJeudi =(
		('no', 'Ne viens pas'),
		('1630', '16h30'),
		('1700', '17h00'),
		('1730', '17h30'),
		('1800', '18h00'),
		('1830', '18h30'),
		)
	DebutFrequentationVendredi =(
		('no', 'Ne Viens pas'),
        ('730', '7h30'),
        ('800', '8h00'),
        ('830', '8h30'),
        ('900', '9h00'),
        ('930', '9h30'),
        )
	FinFrequentationVendredi = (
		('no', 'Ne viens pas'),
		('1630', '16h30'),
		('1700', '17h00'),
		('1730', '17h30'),
		('1800', '18h00'),
		('1830', '18h30'),
		)

	ArriveLundi = models.CharField(max_length=3, choices=DebutFrequentationLundi, default='')
	PartLundi = models.CharField(max_length=4, choices=FinFrequentationLundi, default='')
	ArriveMardi = models.CharField(max_length=3, choices=DebutFrequentationMardi, default='')
	PartMardi = models.CharField(max_length=4, choices=FinFrequentationMardi, default='')
	ArriveMercredi = models.CharField(max_length=3, choices=DebutFrequentationMercredi, default='')
	PartMercredi = models.CharField(max_length=4, choices=FinFrequentationMercredi, default='')
	ArriveJeudi = models.CharField(max_length=3, choices=DebutFrequentationJeudi, default='')
	PartJeudi = models.CharField(max_length=4, choices=FinFrequentationJeudi, default='')
	ArriveVendredi = models.CharField(max_length=3, choices=DebutFrequentationVendredi, default='')
	PartVendredi = models.CharField(max_length=4, choices=FinFrequentationVendredi, default='')

	def __str__(self):
		return self.nom_Enfant

	def __str__(self):
		return self.Prenom_Enfant

	def __str__(self):
		return self.Date_De_Naisaance

	def __str__(self):
		return self.ArriveLundi
	
	def __str__(self):
		return self.PartLundi
	
	def __str__(self):
		return self.ArriveMardi
	
	def __str__(self):
		return self.PartMardi
	
	def __str__(self):
		return self.ArriveMercredi
	
	def __str__(self):
		return self.PartMercredi

	def __str__(self):
		return self.ArriveJeudi

	def __str__(self):
		return self.PartJeudi

	def __str__(self):
		return self.ArriveVendredi

	def __str__(self):
		return self.PartVendredi


