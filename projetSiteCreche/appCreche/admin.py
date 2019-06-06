
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, Enfant, Parent, Employe, OffreEmploi, EnfantEnAttente, EnfantPresent,  EnfantPreinscrit
from .validateurs import *
	
class DetailsEnfant(admin.ModelAdmin):
	
	list_display = ['nom','prenom', 'Parents']
	

class DetailParent(admin.ModelAdmin):

	list_display=['prenom_Mere','prenom_Pere']
	

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email','is_Parent', 'is_Employe']

class DetailOffres(admin.ModelAdmin):
	list_display=['intituleDuPoste']

class DetailEnfantEnAttente(admin.ModelAdmin):
	list_display=['Enfant']

class DetailEnfantPresent(admin.ModelAdmin):
	list_display=['Enfant']

class DetailEnfantPreinscrit(admin.ModelAdmin):
	list_display=['Enfant']

class DetailEmploye(admin.ModelAdmin):
	list_display=['nom','prenom']



admin.site.register(Enfant, DetailsEnfant)
admin.site.register(Parent, DetailParent)
admin.site.register(Employe, DetailEmploye)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(OffreEmploi, DetailOffres)
admin.site.register(EnfantEnAttente, DetailEnfantEnAttente)
admin.site.register(EnfantPresent,DetailEnfantPresent)
admin.site.register(EnfantPreinscrit,DetailEnfantPreinscrit)
