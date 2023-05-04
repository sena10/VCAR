"""carro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import index, base, alugueis, visu, index2, contato
from aluguel import views


urlpatterns = [
    path('', index, name='index'),
    path('index2', index2, name='index2'),
    path('contato', contato, name='contato'),
    path('base', base, name='base'),
    path('alugueis', alugueis, name='alugueis'),
    path('visu', visu, name='visu' ),
    path('registration/', views.registration,name='registration'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout,name='logout'),
]
