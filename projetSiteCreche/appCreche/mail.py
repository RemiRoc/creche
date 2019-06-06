from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from appCreche.token import account_activation_token
from appCreche.models import CustomUser


def sendConfirmationMail(message, to):
    return send_mail(subject="Activation du Compte",
                     message=message,
                     html_message=message,
                     from_email='asso.gros.calin@gmail.com',
                     recipient_list=[to],
                     fail_silently=False,
                     )


#Fonction permettant d'envoyer un mail à l'utilisateur lors de la création de son compte pour l'activer.



def createLink(user):
    uid = urlsafe_base64_encode(force_bytes(user.email))
    # ^ encode l'email de l'utilisateur dans l'url.
    token = account_activation_token.make_token(user)
    # ^  Créé un token aléatoire a placer dans le l'url .
    return "/appCreche/account/activate/{0}/{1}".format(uid, token)

#Créer le lien d'activation du compte. le Token étant une valeur aléatoire et l'uid l'encodage de l'email de l'utilisateur.