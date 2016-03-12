# ask URL Configuration
from django.conf.urls import url, include, patterns
from django.contrib import admin

urlpatterns = [
  url(r'^', include('qa.urls')),
  url(r'^admin/', admin.site.urls),
]
