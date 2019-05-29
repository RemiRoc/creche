from django.urls import path
from . import views

app_name = 'appCreche'
urlpatterns = [

    path('index/', views.index, name='index'),
    path('equipe/', views.equipe, name='equipe'),
    path('contribuer/', views.contribuer, name='Contribuer'),
    path('recrutement/', views.recrutement, name='recrutement'),
    path('inscription/', views.inscription.as_view(), name='inscription'),
    path('inscriptionEnfant/', views.inscriptionEnfant, name='inscriptionEnfant'),
    path('deposFacture/', views.deposFactures, name='deposFacture'),
    path('petitesAnnonces/',views.petitesAnnonces, name='petitesAnnonces'),
   
    path('inscritEmploye/', views.inscritEmploye, name='inscritEmploye'),
    path('monCompte/',views.monCompte, name='monCompte'),
]