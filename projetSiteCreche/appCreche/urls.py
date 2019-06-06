from django.urls import path
from . import views

app_name = 'appCreche'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('recrutement/', views.recrutement, name='recrutement'),
    path('inscription/', views.inscription, name='inscription'),
    path('inscriptionEnfant/', views.inscriptionEnfant, name='inscriptionEnfant'),
    path('deposFacture/', views.deposFactures, name='deposFacture'),
    path('projetPedagogique/',views.projetPedagogique, name='projetPedagogique'),
    path('inscritEmploye/', views.inscritEmploye, name='inscritEmploye'),
    path('monCompte/',views.monCompte, name='monCompte'),
    path('account/activate/<str:uid>/<str:token>', views.activate, name='activate'),
]


"""
Le nom de l'application : appCreche

les différentes urls du projet, 
celles-ci renvoient vers les views, qui sont les "fonctions", permettant d'afficher 
différentes choses ( formulaire principalements ici )
mais également de récupérer les valeurs des models pour les appeller plus tard dans les fichiers html.
"""