from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
import re
def validate_tel(value):
	telVal = re.match("(?:(?:\+|00)|0)[6-7](\d{2}){4}", str(value))
	if(telVal is None):
		raise ValidationError(
			_('%(value)s n\'est pas un numéro de téléphone valide'),
			params={'value': value},
		)
	else:
		return value

def validate_carac(value):
	nom = re.match("((?:[A-Z])([a-z |é|è|ê|\s|-]){1,50}([A-Z]{0,1})([a-z | é|è|ê|\s|-]){1,50})", str(value))
	if(nom is None):
		raise ValidationError(
			_('%(value)s n\'est pas valide'),
			params={'value': value},
		)
	else:
		return value


def validate_adresse(value):
	adresse = re.match("(?:[1-9]{1,4}|[A-Z]*)([a-z |é|è|ê|\s|-]){1,50}(([A-Z]{0,1})([a-z|é|è|ê|\s|-]){1,50})*", str(value))
	if(adresse is None):
		raise ValidationError(
			_('%(value)s n\'est pas une adresse valide (Exemple : 1248 bis route du Soleil )'),
			params={'value': value},
		)
	else:
		return value

from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize= value.size
    
    if filesize > 5242880:
        raise ValidationError("La taille maximum d'un fichier ne peut dépasser 5MB")
    else:
        return value