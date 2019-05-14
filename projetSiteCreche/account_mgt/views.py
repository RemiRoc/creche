from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate, login, logout
from account_mgt.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from account_mgt.forms import CustomLoginForm, CustomRegisterForm, CustomChangeForm
from account_mgt.token import account_activation_token
from account_mgt.mail import sendConfirmationMail, createLink
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse




def home(request):
    if not request.user.is_authenticated:return signin(request)
    return profile(request, request.user)

def signin(request):
    """Login view"""
    if request.user.is_authenticated:return HttpResponseRedirect(reverse('user_profile:profile'))
    if not request.method == "POST":
        return render(request, 'login.html', {'form' : CustomLoginForm(), 'breadcrumb' : "Login",})
    form = CustomLoginForm(request.POST)
    if not form.is_valid():
        return render(request, 'login.html', {'form' : form, 'breadcrumb' : "Login",})
    email = form.cleaned_data.get('email')
    password = form.cleaned_data.get('password')
    user = authenticate(username=email, password=password)
    login(request, user)
    request.method = "GET"
    return HttpResponseRedirect(reverse('user_profile:profile'))

def register(request):
    """Register view"""
    if request.user.is_authenticated:return profile(request, request.user)
    if not request.method == "POST":
        return render(request, 'register.html', {'form' : CustomRegisterForm(), 'breadcrumb' : "Register",})
    form = CustomRegisterForm(request.POST)
    if not form.is_valid():
        return render(request, 'register.html', {'form' : form, 'breadcrumb' : "Register",})
    to_email=form.cleaned_data.get('email')
    user = User.objects.get(email=to_email)
    current_site = get_current_site(request)
    activation_link = createLink(user)
    activation_link = "http://{0}{1}".format(current_site, activation_link)
    message = render_to_string('register_email_template.html', {'username': user.first_name, 'link': activation_link,})
    email = sendConfirmationMail(message=message, to=[to_email])
    return HttpResponseRedirect(reverse('website:index'))

def disconnect(request):
    """Logout view"""
    logout(request)
    return HttpResponseRedirect(reverse('website:index'))

def reset_complete(request):
    """Reset complete view"""
    return render(request, 'password-reset-complete.html')

def activate(request, uid, token):
    """Account activation view""" 
    try:
        uid = urlsafe_base64_decode(uid).decode()
        user = User.objects.get(email=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        # activate user and login:
        user.is_active = True
        user.save()

        return signin(request)

    else:
        return HttpResponse('Activation link is invalid!')

def password_change(request):
    """Change password view"""
    if not request.user.is_authenticated:return signin(request)
    if not request.method == "POST":
        return render(request, 'password-change-form.html', {'form' : CustomChangeForm(request.user), 'breadcrumb' : "ChangePassword",})
    form = CustomChangeForm(request.user ,request.POST)
    if not form.is_valid():
        return render(request, 'password-change-form.html', {'form' : form, 'breadcrumb' : "ChangePassword",})
    user = request.user
    if user is not None and user.is_active:
        user.set_password(form.cleaned_data.get('new_password'))
        user.save()
        return disconnect(request)
    return HttpResponse('Une erreur est survenue')

def delete_account(request):
    """DELETE USER ACCOUNT"""
    if not request.user.is_authenticated:return signin(request)
    user = request.user
    if user is not None and user.is_active:
        user.is_active = False
        user.save()
        return disconnect(request)
    return HttpResponse('Une erreur est survenue')