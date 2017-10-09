"""url_practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from mysite import views

my_patterns = [
    url(r'^company/$', views.company),
]
urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^(\d{1})/$', views.index, name='tv-url'),
    url(r'^about/(?P<author_no>[0|1|2|3])/$', views.about),
    url(r'^list/(?P<list_date>\d{4}/\d{1,2}/\d{1,2})$', views.listing),
    url(r'^post/(\d{4})/(\d{1,2})/(\d{1,2})/(\d{1,3})$', views.post, name='post-url'),
    url(r'^info/', include(my_patterns)),
]
