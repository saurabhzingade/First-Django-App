"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('analyze',views.analyze,name="analyze"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    # path('removepunc',views.removePunc,name="removePunc"),
    # path('capitalf', views.capfirst, name="capfirst"),
    # path('newlineremove', views.newlineremove, name="newlineremove"),
    # path(' ', views.spaceremove, name="spaceremove"),
    # path('charcount', views.charcount, name="charcount")
    # path('',views.index,name="index"),
    # path('about',views.about,name="about"),
    # path('nav',views.nav,name="nav")
]
