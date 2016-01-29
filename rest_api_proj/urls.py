from django.conf.urls import patterns, url, include
from django.contrib import admin
from rest_api_app import views

urlpatterns = patterns('',
    url(r'^auth/', include('djoser.urls.authtoken')),
)

urlpatterns += [
    url(r'^admin/', admin.site.urls),
    url(r'^tables/$', views.table_list),
    url(r'^tables/(?P<ownerId>[0-9]+)/$', views.table_detail),
    url(r'^servertables/', views.get_server_tables),
    url(r'^makerequest/(?P<ownerId>[0-9]+)/$', views.make_table_request),
    url(r'^gettableaddr/', views.get_table_by_addr),

    url(r'^createtable/', views.create_table),
    url(r'^alltables/', views.get_all_tables),
]