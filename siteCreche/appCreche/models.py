from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Enfant(models.Model):
	id_Enfant = models.ForeignKey(Parent, on_delete=models.CASCADE)
	nom_Enfant = models.CharField(max_length=20)
	Prenom_Enfant = models.CharField(max_length=20)
	Date_De_Naisaance = models.DateTimeField('Date de Naissance')
	DebutFrequentationLundi =(
		('', 'Ne Viens pas'),
        ('730', '7h30'),
        ('800', '8h00'),
        ('830', '8h30'),
        ('900', '9h00'),
        ('930', '9h30'),
        )
	FinFrequentationLundi =(
		('', 'Ne viens pas'),
		('1630', '16h30'),
		('1700', '17h00'),
		('1730', '17h30'),
		('1800', '18h00'),
		('1830', '18h30'),
		)
	DebutFrequentationMardi = (
		('', 'Ne Viens pas'),
        ('730', '7h30'),
        ('800', '8h00'),
        ('830', '8h30'),
        ('900', '9h00'),
        ('930', '9h30'),
        )
	FinFrequentationMardi = (
		('', 'Ne viens pas'),
		('1630', '16h30'),
		('1700', '17h00'),
		('1730', '17h30'),
		('1800', '18h00'),
		('1830', '18h30'),
		)
	DebutFrequentationMercredi =  (
		('', 'Ne Viens pas'),
        ('730', '7h30'),
        ('800', '8h00'),
        ('830', '8h30'),
        ('900', '9h00'),
        ('930', '9h30'),
        )
	FinFrequentationMercredi = (
		('', 'Ne viens pas'),
		('1630', '16h30'),
		('1700', '17h00'),
		('1730', '17h30'),
		('1800', '18h00'),
		('1830', '18h30'),
		)
	DebutFrequentationJeudi = (
		('', 'Ne Viens pas'),
        ('730', '7h30'),
        ('800', '8h00'),
        ('830', '8h30'),
        ('900', '9h00'),
        ('930', '9h30'),
        )
	FinFrequentationJeudi =(
		('', 'Ne viens pas'),
		('1630', '16h30'),
		('1700', '17h00'),
		('1730', '17h30'),
		('1800', '18h00'),
		('1830', '18h30'),
		)
	DebutFrequentationVendredi =(
		('', 'Ne Viens pas'),
        ('730', '7h30'),
        ('800', '8h00'),
        ('830', '8h30'),
        ('900', '9h00'),
        ('930', '9h30'),
        )
	FinFrequentationVendredi = (
		('', 'Ne viens pas'),
		('1630', '16h30'),
		('1700', '17h00'),
		('1730', '17h30'),
		('1800', '18h00'),
		('1830', '18h30'),
		)

	ArriveLundi = models.CharField(max_length=3, choices=DebutFrequentationLundii, default='')
	PartLundi = models.CharField(max_length=4, choices=FinFrequentationLundii, default='')
	ArriveMardi = models.CharField(max_length=3, choices=DebutFrequentationMardii, default='')
	PartMardi = models.CharField(max_length=4, choices=FinFrequentationMardii, default='')
	ArriveMercredi = models.CharField(max_length=3, choices=DebutFrequentationMercredii, default='')
	PartMercredi = models.CharField(max_length=4, choices=FinFrequentationMercredii, default='')
	ArriveJeudi = models.CharField(max_length=3, choices=DebutFrequentationJeudii, default='')
	PartJeudi = models.CharField(max_length=4, choices=FinFrequentationJeudii, default='')
	ArriveVendredi = models.CharField(max_length=3, choices=DebutFrequentationVendredii, default='')
	PartVendredi = models.CharField(max_length=4, choices=FinFrequentationVendredii, default='')

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


