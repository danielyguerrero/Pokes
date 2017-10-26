from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="dashboard"),
    url(r'^poke/(?P<id>\d+)$', views.poke, name='poke'),
#<a href="/poke/{{quote.id}}}">Poke</a>
]


#The current path, pokes/poke/, didn't match any of these. 