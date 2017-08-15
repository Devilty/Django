"""Devil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from . import view
from . import search
from . import searchpost
from . import home

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^admin/', admin.site.urls),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', searchpost.search_post),
    url(r'^home$', home.home),
    url(r'^blog/', include('MyModel.urls', namespace='blog')),
]

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
