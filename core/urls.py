from django import views
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.homeview,name='home'),
    path('welcome/',views.welcomeview,name="welcome"),
    path('register/',views.registerview,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name='common/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='common/logout.html'),name='logout'),
    path('reset_pass/',auth_views.PasswordResetView.as_view(template_name='common/password_reset.html'),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='common/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='common/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name='common/password_reset_complete.html'),name='password_reset_complete'),
]