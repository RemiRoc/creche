
from django.contrib import admin
from .models import Enfant



class DetailsEnfant(admin.ModelAdmin):
	list_display = ('nom_Enfant','Prenom_Enfant')


admin.site.register(Enfant) 