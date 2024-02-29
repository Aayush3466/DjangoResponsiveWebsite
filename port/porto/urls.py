from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'porto'
urlpatterns = [
    path('', views.index, name='porto'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='porto/login.html', authentication_form=LoginForm), name='login')
]