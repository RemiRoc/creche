from django.contrib.auth.hashers import check_password
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import auth
from django.test import TestCase, Client

from unittest.mock import Mock, MagicMock, patch

from account_mgt.models import User
from account_mgt.token import account_activation_token
from account_mgt.forms import *
from account_mgt.mail import createLink



# Create your tests here.

class TestCaseAccountMGT(TestCase):

	def setUp(self):
		self.si = forms.ValidationError(_('Incorrect email or password: Please enter valid credentials.'),code='invalid_credentials')
		self.na = forms.ValidationError(_('This account is not activated.'),code='account_not_activated')

		self.em = forms.ValidationError(_('Please enter a valid email'), code='invalid credentials')
		self.pa = forms.ValidationError(_('Please enter a valid password'), code='invalid credentials')
		self.cp = forms.ValidationError(_('Confirm password field does not match password'),code='confirm_password_not_match')
		self.fn = forms.ValidationError(_('Your first name is invalid (Field required)'),code='invalid credentials')
		self.ln = forms.ValidationError(_('Your last name is invalid (Field required)'),code='invalid credentials')
		self.pn = forms.ValidationError(_('Phone number incorrect'),code='invalid credentials')
		self.sz = forms.ValidationError(_('Informations given are too long'),code='invalid credentials')
		self.at = forms.ValidationError(_('You must agree with terms and conditions'),code='agree_toc_false')
		self.us = forms.ValidationError(_('User already exists.'),code='user_exists')

	#TESTS GÉNÉRIQUES INSCRITION
	def cas_nominal_inscription(self, form_data):
		f = CustomRegisterForm(form_data)
		self.assertEqual(f.is_valid(), True)

		c = Client()
		response = c.post('/account/register/', form_data, follow=True)

		users = User.objects.all()
		u = User.objects.get(email=form_data.get('email'))

		self.assertEqual(response.status_code, 200)

		self.assertEqual(len(users), 1)
		self.assertEqual(u.email, form_data.get('email'))
		self.assertEqual(check_password(form_data.get('password'), u.password), True)
		self.assertEqual(u.first_name, form_data.get('first_name'))
		self.assertEqual(u.last_name, form_data.get('last_name'))
		self.assertEqual(u.phone_number, form_data.get('phone_number'))
		self.assertEqual(u.company, form_data.get('company'))
		self.assertEqual(u.address, form_data.get('address'))
		self.assertEqual(u.is_active, False)

	def cas_robustesse_inscription(self, form_data, t_error):
		n1 = User.objects.all()
		f = CustomRegisterForm(form_data)
		self.assertEqual(f.is_valid(), False)	
		with self.assertRaises(ValidationError) as cm:
			f.clean()
		e = cm.exception
		self.assertEqual(e.code, t_error.code)
		self.assertEqual(e.message, t_error.message)

		c = Client()
		response = c.post('/account/register/', form_data, follow=True)
		n2 = User.objects.all()
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(n1), len(n2))

	#TESTS GÉNÉRIQUES CONNEXION
	def cas_nominal_connexion(self, form_data):
		f = CustomLoginForm(form_data)
		self.assertEqual(f.is_valid(), True)

		c = Client()
		response = c.post('/account/signin/', form_data, follow=True)
		self.assertRedirects(
			response, '/user/profile/', status_code=302,
			target_status_code=200, msg_prefix='',
			fetch_redirect_response=True
		)
		self.assertEqual(response.status_code, 200)
		


	def cas_robustesse_connexion(self, form_data, t_error):
		f = CustomLoginForm(form_data)
		self.assertEqual(f.is_valid(), False)
		with self.assertRaises(ValidationError) as cm:
			f.clean()
		e = cm.exception
		self.assertEqual(e.code, t_error.code)
		self.assertEqual(e.message, t_error.message)
		c = Client()
		response = c.post('/account/signin/', form_data, follow=True)
		self.assertEqual(response.status_code, 200)

	def cas_activation_link(self, url, user, cas_robustesse = False):
		c = Client()
		response = c.get(url, follow=True)
		self.assertEqual(response.status_code, 200)
		#UPDATE USER OTHERWISE is_active = whatever before the test was launched
		user=User.objects.get(email=user.email)
		if not cas_robustesse:
			self.assertEqual(user.is_active, True)
		else:
			self.assertEqual(user.is_active, False)
			
	"""
		EXIGENCES COUVERTES PAR LE SCÉNARIO :
		#CDC100.3_EXI_0000
		#CDC100.3_EXI_0010
		#CDC100.3_EXI_0020
		#CDC100.3_EXI_7000
		#CDC100.3_EXI_7010
		#CDC100.3_EXI_7020
		#CDC100.3_EXI_7030
		#CDC100.3_EXI_7040
		#CDC100.3_EXI_7050
	"""
	#si ligne décommentée ajouter mock en paramètre de fonction
	#@patch('account_mgt.mail.sendConfirmationMail')
	def test_scenario(self):
		#TEST INSCRIPTION
		#TST_0030
		from account_mgt.views import register
		from account_mgt.mail import sendConfirmationMail 
		form_data={'email': 'toto@test.com',
		'password': 'azertY1+','confirm_password' : 'azertY1+',
		'first_name': 'tutu','last_name': 'toto','phone_number':'',
		'company':'', 'address':'', 'agree_toc':False
		}
		self.cas_robustesse_inscription(form_data, self.at)

		
		#TEST INSCRIPTION
		#TST_0040
		form_data={'email': 'toto@test',
		'password': 'azertY1+','confirm_password' : 'azertY1+',
		'first_name': 'tutu','last_name': 'toto','phone_number':'',
		'company':'', 'address':'', 'agree_toc':True
		}
		self.cas_robustesse_inscription(form_data, self.em)


		#TEST INSCRIPTION
		#TST_0050
		form_data={'email': 'tototototototototototototototototototototo\
		tototototototototototototototototototototototototototo@toto\
		tototototototototototototototototototototototototototototot\
		ototototototototototototototototo.com',
		'password': 'azertY1+','confirm_password' : 'azertY1+',
		'first_name': 'tutu','last_name': 'toto','phone_number':'',
		'company':'', 'address':'', 'agree_toc':True
		}
		self.cas_robustesse_inscription(form_data, self.em)

		
		#TEST INSCRIPTION
		#TST_0060
		form_data={'email': 'toto@test.com',
		'password': 'azertY1+azertY1+azertY1+azertY1+azertY1+azertY1+azertY1\
		+azertY1+azertY1+azertY1+azertY1+azertY1+azertY1+azertY1+azertY1+aze\
		rtY1+1234567890','confirm_password' : 'azertY1+azertY1+azertY1+azert\
		Y1+azertY1+azertY1+azertY1+azertY1+azertY1+azertY1+azertY1+azertY1+a\
		zertY1+azertY1+azertY1+azertY1+1234567890', 'first_name': 'tutu',
		'last_name': 'toto','phone_number':'','company':'', 'address':'',
		'agree_toc':True
		}
		self.cas_robustesse_inscription(form_data, self.pa)

		
		#TEST INSCRIPTION
		#TST_0070
		form_data={'email': 'toto@test.com',
		'password': 'aZ1+','confirm_password' : 'aZ1+', 'first_name': 'tutu',
		'last_name': 'toto','phone_number':'','company':'', 'address':'',
		'agree_toc':True
		}
		self.cas_robustesse_inscription(form_data, self.pa)

		
		#TEST INSCRIPTION
		#TST_0080
		form_data={'email': 'toto@test.com',
		'password': 'azertY1+','confirm_password' : 'azertY2$',
		'first_name': 'tutu','last_name': 'toto','phone_number':'',
		'company':'', 'address':'', 'agree_toc':True
		}
		self.cas_robustesse_inscription(form_data, self.cp)

		
		#TEST INSCRIPTION
		#TST_0090
		form_data={'email': 'toto@test.com',
		'password': 'azertY1+','confirm_password' : 'azertY1+',
		'first_name': 'tutu','last_name': 'tatatatatatatatatata\
		tatatatatatatatatatatatatatatata','phone_number':'',
		'company':'', 'address':'', 'agree_toc':True
		}
		self.cas_robustesse_inscription(form_data, self.ln)

		
		#TEST INSCRIPTION
		#TST_0100
		form_data={'email': 'toto@test.com',
		'password': 'azertY1+','confirm_password' : 'azertY1+',
		'first_name': 'tatatatatatatatatatatatatatatatatatatat\
		atatatatatata','last_name': 'toto','phone_number':'',
		'company':'', 'address':'', 'agree_toc':True
		}
		self.cas_robustesse_inscription(form_data, self.fn)

		
		#TEST INSCRIPTION
		#TST_0110
		form_data={'email': 'toto@test.com',
		'password': 'azertY1+','confirm_password' : 'azertY1+',
		'first_name': 'tutu','last_name': 'toto','phone_number':'',
		'company':'tatatatatatatatatatatatatatatatatatatat\
		atatatatatatatatatatatatatatatatatatatatatatatatatat\
		atatatatatata', 'address':'', 'agree_toc':True
		}
		self.cas_robustesse_inscription(form_data, self.sz)

		
		#TEST INSCRIPTION
		#TST_0120
		form_data={'email': 'toto@test.com',
		'password': 'azertY1+','confirm_password' : 'azertY1+',
		'first_name': 'tutu','last_name': 'toto','phone_number':'',
		'company':'', 'address':'tatatatatatatatatatatatatatatatat\
		atatatatatatatatatatatatatatatatatatatatatatatatatatatatat\
		atatatatatata', 'agree_toc':True
		}
		self.cas_robustesse_inscription(form_data, self.sz)

		
		#TEST INSCRIPTION
		#TST_0130
		form_data={'email': 'toto@test.com',
		'password': 'azertY1+','confirm_password' : 'azertY1+',
		'first_name': 'tutu','last_name': 'toto','phone_number':'+3630',
		'company':'', 'address':'', 'agree_toc':True
		}
		self.cas_robustesse_inscription(form_data, self.pn)

		
		#TEST INSCRIPTION
		#TST_0140
		form_data={'email': 'toto@test.com',
		'password': 'azertY1+','confirm_password' : 'azertY1+',
		'first_name': 'tutu','last_name': 'toto','phone_number':'+33669\
		922558811447700', 'company':'', 'address':'', 'agree_toc':True
		}
		self.cas_robustesse_inscription(form_data, self.pn)

		
		#TEST INSCRIPTION
		#TST_0150
		form_data={'email': 'toto@test.com',
		'password': 'azertY1+','confirm_password' : 'azertY1+',
		'first_name': 'tutu','last_name': 'toto','phone_number':'060708091011',
		'company':'', 'address':'', 'agree_toc':True
		}
		self.cas_robustesse_inscription(form_data, self.pn)


		#TEST INSCRIPTION
		#TST_0020
		form_data={'email': 'toto@test.com',
		'password': 'azertY1+','confirm_password' : 'azertY1+',
		'first_name': 'tutu','last_name': 'toto','phone_number':'',
		'company':'', 'address':'', 'agree_toc':True
		}
		self.cas_nominal_inscription(form_data)
		#email non-testable pour le moment
		#mock.assert_called()
		

		#TEST INSCRIPTION
		#TST_0160
		self.cas_robustesse_inscription(form_data, self.us)

		#TEST CONNEXION
		#TST_0020
		form_data={'email': 'toto@test.com', 'password':'azertU1+'}
		self.cas_robustesse_connexion(form_data, self.si)

		#TEST CONNEXION
		#TST_0030
		form_data={'email': 'toto@test.com', 'password':'azertY1+'}
		self.cas_robustesse_connexion(form_data, self.na)

		#TEST ACTIVATION
		#TST_0020
		u = User.objects.get(email=form_data.get('email'))
		uid = urlsafe_base64_encode(force_bytes(u.email))
		token = "iNvAlId" 
		activation_link = "/account/activate/{0}/{1}".format(uid, token)
		self.cas_activation_link(activation_link, u, True)

		#TEST ACTIVATION
		#TST_0030
		uid = 'iNvAlId'
		token = account_activation_token.make_token(u)
		activation_link = "/account/activate/{0}/{1}".format(uid, token)
		self.cas_activation_link(activation_link, u, True)


		#TEST ACTIVATION
		#TST_0010
		activation_link = createLink(u)
		self.cas_activation_link(activation_link, u, False)
		u = User.objects.get(email=form_data.get('email'))

		#TEST CONNEXION
		#TST_0010
		form_data={'email': 'toto@test.com', 'password':'azertY1+'}
		self.cas_nominal_connexion(form_data)
		u = User.objects.get(email=form_data.get('email'))