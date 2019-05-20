# users/forms.py
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Enfant, Parent, ListeDAttente
from . import horaires

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email','is_Parent', 'is_Employe')



class EnfantCreationForm(ModelForm):
	class Meta:
		model = Enfant
		fields = '__all__'
class ParentCreationForm(ModelForm):
	class Meta: 
		model= Parent
		fields= '__all__'