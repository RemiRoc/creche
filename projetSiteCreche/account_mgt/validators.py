from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

def phone_validator():
	return RegexValidator(regex=r'^\+1?\d{9,15}$', message="Phone number must be entered in the format: '+00000000'. Up to 15 digits allowed.")

def password_validator():
	return RegexValidator(regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^a-zA-Z\d\s:])(.{8,128}$)', message="Password must be : 8 characters\
		, 1 upper case, 1 lower case, 1 digit and a non-alphanumeric character")