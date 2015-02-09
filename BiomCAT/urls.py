from django.conf.urls import patterns, url

from BiomCAT import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^training/$', views.training, name='training'),
    url(r'^question/$', views.question, name='question'),
    (r'^login/$', 'django.contrib.auth.views.login'),
)