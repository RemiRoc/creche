# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
"""
class PasswordResetView(generic.CreateView):
	success_url = reverse_lazy('password_reverse_done')
	template_name = 'password_reset_form.html'

"""