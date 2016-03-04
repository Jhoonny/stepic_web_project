# ask URL Configuration

from django.conf.urls import url
from stepic_web.ask.qa import views

urlpatterns = (url("^$", views.test, name="first_page"),
               url("^login/$",  views.test, name="login"),
               url("^signup/$",  views.test, name="signup"),
               url("^question/(?P<pk>\d+)/$",  views.test, name="question"),
               url("^ask/",  views.test, name="ask"),
               url("^popular/$",  views.test, name="popular"),
               url("^new/$",  views.test, name="new")
               )