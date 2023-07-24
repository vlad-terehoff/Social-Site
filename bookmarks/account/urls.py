from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


#  path('login/', views.user_login, name='login') - старый url входа
urlpatterns = [path('', views.dashboard, name='dashboard'),
               path('', include('django.contrib.auth.urls')),
               path('register/', views.register, name='register'),
               path('edit/', views.edit, name='edit')
               ]