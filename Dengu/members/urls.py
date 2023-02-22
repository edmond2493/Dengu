from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('register_user', views.register_user, name='register_user'),
    path('password', auth_views.PasswordChangeView.as_view(template_name='password.html', success_url="../profile")),
]
