
from django.contrib import admin
from .models import Enfant, Parent, Contributeur, Employe

#class DetailsEnfant(admin.ModelAdmin):
#	list_display = ('nom_Enfant','Prenom_Enfant')
#	fields = ('nom_Enfant', 'Prenom_Enfant')

admin.site.register(Enfant)
admin.site.register(Parent)
admin.site.register(Contributeur)
admin.site.register(Employe)