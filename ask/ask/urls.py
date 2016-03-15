from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from qa import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.auth_login),
    url(r'^signup/', views.signup),
    url(r'^question/(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^ask/', views.add_question),
    url(r'^answer/', views.add_answer),
    url(r'^popular/', views.popular),
    url(r'^new/', views.test),
)