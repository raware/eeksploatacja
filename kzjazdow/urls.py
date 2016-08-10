from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.lista_zjazdow, name='lista_zjazdow'),
	url(r'^zjazdy/(?P<pk>[0-9]+)/$', views.szczegoly_zjazdu, name='szczegoly_zjazdu'),
	url(r'^zjazdy/dodaj_zjazd/$', views.dodaj_zjazd, name='dodaj_zjazd'),
	url(r'^zjazdy/edytuj_zjazd/(?P<pk>[0-9]+)/$', views.edytuj_zjazd, name='edytuj_zjazd'),
	url(r'^zjazdy/(?P<pk>[0-9]+)/usun/$', views.usun_zjazd, name='usun_zjazd'),
	url(r'^zjazdy/test/', views.test, name='test'),
]