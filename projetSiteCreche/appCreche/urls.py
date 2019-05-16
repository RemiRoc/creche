from django.urls import path
from . import views


urlpatterns = [

    path('index/', views.index, name='index'),
    path('equipe/', views.equipe, name='equipe'),
    path('contribuer/', views.contribuer, name='Contribuer'),
    path('recrutement/', views.recrutement, name='recrutement'),
    path('inscription/', views.inscription, name='inscription'),
    path('inscriptionEnfant/', views.inscriptionEnfant, name='inscriptionEnfant'),
    path('petitesAnnonces/',views.petitesAnnonces, name='petitesAnnonces'),
    path('modificationEnfantPonctuel/',views.modificationEnfantPonctuel, name='modificationEnfantPonctuel'),
    path('tableauEmploye/', views.tableauEmploye, name='tableauEmploye'),
    path('monCompte/',views.monCompte, name='monCompte'),
]