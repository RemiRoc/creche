from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from appCreche.token import account_activation_token
from appCreche.models import CustomUser


def sendConfirmationMail(message, to):
    return send_mail(subject="Please activate your account",
                     message=message,
                     html_message=message,
                     from_email='asso.gros.calin@gmail.com',
                     recipient_list=[to],
                     fail_silently=False,
                     )


def createLink(user):
    uid = urlsafe_base64_encode(force_bytes(user.email))
    token = account_activation_token.make_token(user)
    return "/appCreche/account/activate/{0}/{1}".format(uid, token)