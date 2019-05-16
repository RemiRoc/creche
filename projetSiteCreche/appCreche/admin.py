
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Enfant, Parent, Contributeur, Employe
#class DetailsEnfant(admin.ModelAdmin):
#	list_display = ('nom_Enfant','Prenom_Enfant')
#	fields = ('nom_Enfant', 'Prenom_Enfant')
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(Enfant)
admin.site.register(Parent)
admin.site.register(Contributeur)
admin.site.register(Employe)


admin.site.register(CustomUser, CustomUserAdmin)