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
from qa.views import bad_route, test

urlpatterns = [
    url(r'^$', test),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/(?P<id>[^/]+)', test),
    url(r'^ask/', test),
    url(r'^popular/', test),
    url(r'^new/', test),
    url(r'^admin/', admin.site.urls),
]