"""MyNotebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from notebook import views as notebook_views
import django.contrib.auth.views
from notebook.views import *

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^table/', table, name = "table"),
    url(r'^addnote/', addnote, name="addnote"),
    url(r'^removenote/(?P<noteId>\d+)/', removenote, name="removenote"),
    url(r'^edit/(?P<noteId>\d+)/', editnote, name="editnote"),
    url(r'^logout/$', logout, name="logout"),
]