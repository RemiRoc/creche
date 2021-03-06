from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from .models import CustomUser

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.email) + six.text_type(timestamp) + six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()


#Créé un Token aléatoire qui sert a vérifier l'email.