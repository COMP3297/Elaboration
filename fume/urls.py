from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.featured, name='featured'),
    url(r'^games/(?P<game_id>\d+)/$', views.games, name='games'),
    url(r'^purchase$', views.purchase, name='purchase'),
    ]