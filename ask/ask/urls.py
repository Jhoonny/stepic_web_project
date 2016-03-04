# ask URL Configuration

"""
from django.conf.urls import url
from stepic_web.ask.qa import views

urlpatterns =(\
  url("^$", views.get_questions, name="first_page", kwargs={"question_type": "new"}),
  url("^login/$",  views.test, name="login"),
  url("^signup/$",  views.test, name="signup"),
  url("^question/(?P<pk>\d+)/$",  views.test, name="question"),
  url("^ask/",  views.test, name="ask"),
  url("^popular/$",  views.get_questions, name="popular", kwargs={"question_type": "popular"}),
  url("^new/$",  views.get_questions, name="new", kwargs={"question_type": "new"})
)
"""
from django.conf.urls import url
from django.contrib import admin
from qa import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'login/$', views.test),
    url(r'signup/$', views.test),
    url(r'question/([1-9]+)/$', views.test),
    url(r'ask/$', views.test),
    url(r'popular/$', views.test),
    url(r'new/$', views.test),
    url(r'^admin/', admin.site.urls),
]