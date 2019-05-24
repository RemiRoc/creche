
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, Enfant, Parent, Contributeur, Employe, OffreEmploi, EnfantEnAttente, EnfantPresent,  EnfantPreinscrit
from .validateurs import *
	
class DetailsEnfant(admin.ModelAdmin):
	
	list_display = ['nom','prenom', 'Parents']
	

class DetailParent(admin.ModelAdmin):

	list_display=['prenom_Mere','prenom_Pere']
	

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email','is_Parent', 'is_Employe', 'is_Contrib']

admin.site.register(Enfant, DetailsEnfant)
admin.site.register(Parent, DetailParent)
admin.site.register(Contributeur)
admin.site.register(Employe)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(OffreEmploi)
admin.site.register(EnfantEnAttente)
admin.site.register(EnfantPresent)
admin.site.register(EnfantPreinscrit)
