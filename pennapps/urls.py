from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('application/', views.application, name='application'),
    path('login/', auth_views.LoginView.as_view(template_name = 'pennapps/login.html')),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('signup/', views.signup, name='signup'),
    path('createUser/', views.create_user, name='create_user'),
    path('base/', views.base, name='base'),
    path('submit-application', views.submit_application, name='submit_application'),

] 
