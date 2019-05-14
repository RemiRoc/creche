from django.urls import path, re_path, include
from account_mgt import views
from django.contrib.auth import views as auth_views
from account_mgt.forms import CustomSetForm

app_name = 'account_mgt'
urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.disconnect, name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password-reset-form.html"), name='reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password-reset-done.html"), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password-reset-confirm.html", form_class=CustomSetForm),name='password_reset_confirm'),
	path('reset/done/', views.reset_complete, name='password_reset_complete'),
	path('password_change/', views.password_change, name='password_change'),
    path('register/', views.register, name='register'),
    path('activate/<str:uid>/<str:token>', views.activate, name='activate'),
    path('delete_account/', views.delete_account, name='delete_account')
]


