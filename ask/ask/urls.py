"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
"""
old config urls
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'', sites.urls),
    url(r'^login/', login.site.urls),
    url(r'^signup/', signup.site.urls),
    url(r'^question/(\d+)/', question.site.urls),
    url(r'^ask/', ask.site.urls),
    url(r'^popular/', popular.site.urls),
    url(r'^new/', new.site.urls),
]
"""
from django.conf.urls import url, patterns

ulrpatterns = patterns("qa.views",
                       url("^$", "test", name="first_page"),
                       url("^login/$", "test", name="login"),
                       url("^signup/$", "test", name="signup"),
                       url("^question/(?P<pk>\d+)/$", "test", name="question"),
                       url("^ask/", "test", name="ask"),
                       url("^popular/$", "test", name="popular"),
                       url("^new/$", "test", name="new")
                       )

)