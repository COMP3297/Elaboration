from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.featured, name='featured'),
    url(r'^games/(?P<game_id>\d+)/$', views.games, name='games'),
    url(r'^purchase/(?P<game_id>\d+)/$', views.purchase, name='purchase'),
    url(r'^purchaseAll$', views.purchaseAll, name='purchaseAll'),
    ]