from django.utils.translation import ugettext_lazy as _
from account_mgt.validators import *
from django.contrib.auth import authenticate
from account_mgt.models import User
from material import *
from django import forms



class CustomLoginForm(forms.Form):
    """This is a custom login form"""
    email_attrs  = {'autofocus': '','required':'True',}	
    email_errors = {'invalid': _('The \'Email\' field is invalid'),}
    email        = forms.EmailField(widget = forms.TextInput(attrs=email_attrs),error_messages=email_errors)
    password     = forms.CharField(widget=forms.PasswordInput)
    layout       = Layout(
        Fieldset("Connexion",'email','password',)
    )

    class Meta:
        models = User
        fields = ('email', 'password')
    
    def clean(self):
        cleaned_data = super(CustomLoginForm, self).clean()        
        
        #error message
        f = forms.ValidationError(_('Incorrect email or password: Please enter valid credentials.'),code='invalid_credentials')
        
        email    = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        
        #Check form
        if not email or not password: raise f
        #Auth user
        user = authenticate(username=email, password=password)
        #Check if user exists
        if user is None:raise f
        
        #Check if account activated
        if not user.is_active:raise forms.ValidationError(_('This account is not activated.'),code='account_not_activated')
        
        return cleaned_data

class CustomRegisterForm(forms.Form):
    """This is a custom register form"""
    
    #error messages and help text
    email_errors  = {'invalid': _('The \'Email\' field is invalid'),}
    phone_help    = "Phone number must be entered in the format: '+00000000'. Up to 15 digits allowed."
    password_help = "Your password must have at least :<br> - 8 characters<br> - 1 upper case<br> \
    - 1 lower case<br> - 1 digit<br> - 1 non-alphanumeric character"

    #email field
    email_attrs = {'autofocus': '','required':'True',}  
    email       = forms.EmailField(widget = forms.TextInput(attrs=email_attrs),error_messages=email_errors, max_length=254)

    #password filed
    password         = forms.CharField(widget=forms.PasswordInput, validators=[password_validator()], max_length=128, help_text=password_help)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm password")

    #mandatory
    first_name = forms.CharField(widget=forms.TextInput, max_length=50)
    last_name  = forms.CharField(widget=forms.TextInput, max_length=50)
    agree_toc  = forms.BooleanField(required=True, label='I agree with the Terms and Conditions')
    
    #not mandatory
    phone_number = forms.CharField(required=False, validators=[phone_validator()], help_text=phone_help, max_length=16)
    company      = forms.CharField(required=False, widget=forms.TextInput, max_length=100)
    address      = forms.CharField(required=False, widget=forms.TextInput, max_length=100)
    
    layout = Layout(
        Fieldset("Register",'email','password','confirm_password','first_name','last_name','phone_number','company', 'address', 'agree_toc',)
    )

    class Meta:
        models = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'company', 'address','password',)
    
    def clean(self):
        cleaned_data = super(CustomRegisterForm, self).clean()
        #error messages

        em = forms.ValidationError(_('Please enter a valid email'), code='invalid credentials')
        pa = forms.ValidationError(_('Please enter a valid password'), code='invalid credentials')
        cp = forms.ValidationError(_('Confirm password field does not match password'),code='confirm_password_not_match')
        fn = forms.ValidationError(_('Your first name is invalid (Field required)'),code='invalid credentials')
        ln = forms.ValidationError(_('Your last name is invalid (Field required)'),code='invalid credentials')
        pn = forms.ValidationError(_('Phone number incorrect'),code='invalid credentials')
        sz = forms.ValidationError(_('Informations given are too long'),code='invalid credentials')
        at = forms.ValidationError(_('You must agree with terms and conditions'),code='agree_toc_false')
        us = forms.ValidationError(_('User already exists.'),code='user_exists')


        #get fields
        email            = self.cleaned_data.get('email')
        password         = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        first_name       = self.cleaned_data.get('first_name')
        last_name        = self.cleaned_data.get('last_name')
        phone_number     = self.cleaned_data.get('phone_number')
        company          = self.cleaned_data.get('company')
        address          = self.cleaned_data.get('address')
        agree_toc        = self.cleaned_data.get('agree_toc')


        #Check form
        if not agree_toc: raise at
        if not email: raise em
        if not password: raise pa
        if not password == confirm_password:
            self.add_error("confirm_password", "This field does not match password")
            raise cp
        if not last_name:raise ln
        if not first_name:raise fn
        
        if not phone_number and not phone_number=="":raise pn
        if not company and not company=="":raise sz
        if not address and not address=="":raise sz

        #Check User already exists
        if (len(User.objects.filter(email=email)) > 0): raise us

        #Save user
        user = User(email=email, last_name=last_name, first_name=first_name, phone_number=phone_number, company=company, address=address)
        user.set_password(password)
        user.is_active=False
        user.save()
        return cleaned_data

class CustomSetForm(forms.Form):
    """This is a custom form for reseting user's passsword """
    #messages
    password_help = "Your password must have at least :<br> - 8 characters<br> - 1 upper case<br> \
    - 1 lower case<br> - 1 digit<br> - 1 non-alphanumeric character"

    #fields
    new_password     = forms.CharField(widget=forms.PasswordInput, label=_("New password"), validators=[password_validator()], help_text=password_help)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label=_("Confirm password"))
    
    layout = Layout(
        Fieldset("Reset password",'new_password','confirm_password',)
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(CustomSetForm, self).__init__(*args, **kwargs)
    
    def clean(self, changePassword=False):
        cleaned_data = super(CustomSetForm, self).clean()
        
        #error messages
        #ep = email/password, cp = confirm password.
        ep = forms.ValidationError(_('Incorrect new password: Please enter valid password.'),code='invalid_password')
        cp = forms.ValidationError(_('Confirm password field does not match password'),code='confirm_password_not_match')

        #get fields
        new_password     = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')


        #Check form
        if not changePassword:
            if not new_password: raise ep
            if not new_password == confirm_password:
                self.add_error("confirm_password", "This field does not match password")
                raise cp
        return cleaned_data


    def save(self, commit=True):
        """
        Saves the new password.
        """
        self.user.set_password(self.cleaned_data["new_password"])
        if commit:
            self.user.save()
        return self.user

class CustomChangeForm(CustomSetForm):
    """This is a custom form for changing user's password"""
    
    #field
    old_password = forms.CharField(label=_("Old password"), widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super(CustomChangeForm, self).clean()
        
        #error messages
        #ep = email/password, cp = confirm password, op = old password.
        op = forms.ValidationError(_('Your old password is incorrect'),code='invalid_credentials')

        #get field
        old_password = self.cleaned_data.get('old_password')

        #Check form
        if not self.user.check_password(old_password):raise op
        return cleaned_data

    field_order = ['old_password', 'new_password', 'confirm_password']