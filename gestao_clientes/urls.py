"""gestao_clientes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from clientes import urls as clientes_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

#from django.contrib.auth.views import LoginView


urlpatterns = [
    path('clientes/',include(clientes_urls)),
        #gregory path('accounts/login/', auth_views.LoginView.as_view())
        #gregory path('logout/', auth_views.logout, name="logout"),
           #osmar path('login/', LoginView.as_view(), name="login"),
            # osmar path('logout/', LoginView.as_view(), name="logout"),
                #Marcos path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
                #Marcos path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




