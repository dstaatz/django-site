from django.conf.urls import url

from . import views

app_name = 'blogs'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='About'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
