"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
=======
    https://docs.djangoproject.com/en/3.0/topics/http/urls/

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
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path
<<<<<<< HEAD

urlpatterns = [
    path('admin/', admin.site.urls),
from home.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

from django.urls import path, include

from contact.views import contact
from home.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('kontakt/', include('contact.urls')),

]
    path('contact/', include('contact.urls')),
    path('product/', include('product.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
