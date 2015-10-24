from django.conf.urls import patterns, url, include
from rest_api_app import views

urlpatterns = patterns('',
    url(r'^auth/', include('djoser.urls.authtoken')),
)

urlpatterns += [
    url(r'^tables/$', views.table_list),
    url(r'^tables/(?P<ownerId>[0-9]+)/$', views.table_detail),
    url(r'^servertables/', views.get_server_tables)
]