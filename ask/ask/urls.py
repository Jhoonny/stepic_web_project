# ask URL Configuration
from django.conf.urls import url
from ask.qa import views

urlpatterns = (\
   # url(r'^$', views.test, name='test'),
   url(r'^login/', views.test, name='login'),
   url(r'^signup/', views.test, name='signup'),
   url(r'^question/\d+/', views.test, name='question'),
   url(r'^ask/', views.test, name='aks'),
   url(r'^popular/', views.test, name='popular'),
   url(r'^new/', views.test, name='new'),

   url(r'^$',views.question_list , name='question_list'),
   url(r'^popular/', , name=''),
   url(r'^question/(?P<id>\d+)/$', views., name=''),
)
