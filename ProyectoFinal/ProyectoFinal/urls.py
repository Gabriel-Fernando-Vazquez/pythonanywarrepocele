"""
URL configuration for ProyectoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Inicio, name='inicio'),
    path('sobre-nosotros', views.SobreNosotros, name = 'sobre-nosotros'),
    path('contacto', views.Contacto, name = 'contacto'),

    # NOTICIAS ORDENADAS SEGUN...
    path('ord-fecha-desc/', views.OrdFechaDesc, name="ord-fecha-desc"),
    path('ord-tit-asc/', views.OrdTitAsc, name="ord-tit-asc"),
    path('ord-tit-desc/', views.OrdTitDesc, name="ord-tit-desc"),

    # URLS DE AUTH
    path('login/', auth.LoginView.as_view(template_name="usuarios/login.html"), name='login'),
    path('logout/', auth.LogoutView.as_view(), name='logout'),

    # URLS USUARIOS
    path('usuarios/', include('apps.usuarios.urls')),

    # URLS NOTICIAS
    path('noticias/', include('apps.noticias.urls')),

    # URLS COMENTARIOS
    path('comentarios/', include('apps.comentarios.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)