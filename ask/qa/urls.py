from django.conf.urls import url, patterns

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^login/', views.login_user, name='login'),
  url(r'^signup/', views.signup, name='signup'),
  url(r'^question/(?P<id>[^/]+)', views.one_quest, name=''),
  url(r'^popular/', views.popular_quests, name=''),
  url(r'^new/', views.test, name=''),
  url(r'^ask/', views.ask_add, name='ask'),
  url(r'^answer/', views.answer_add, name=''),
  url(r'^logout/', views.logout_user, name=''),
]
