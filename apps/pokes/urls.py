from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="dashboard"),
    url(r'^poke/(?P<user_id>\d+)$', views.addPoke, name='addPoke'),
]

