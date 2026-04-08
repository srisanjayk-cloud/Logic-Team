from django.urls import path , include
from django.contrib.auth import views as auth_views
from core import views


urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('new-event/' , views.event_create, name = 'event_create'),
    path('events/', views.event_list, name='events'),
    path('new-project/' , views.project_create, name = 'project_create'),
    path('projects/', views.project_list, name='projects'),

    
]
