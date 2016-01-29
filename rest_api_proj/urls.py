from django.conf.urls import patterns, url, include
from django.contrib import admin
from rest_api_app import views

urlpatterns = patterns('',
    url(r'^auth/', include('djoser.urls.authtoken')),
)

urlpatterns += [
    url(r'^admin/', admin.site.urls),

    url(r'^create_table/', views.create_or_join_table),
    url(r'^all_tables/', views.get_all_tables),
    url(r'^delete_table/', views.delete_table),
    url(r'^users_at_table/', views.get_users_at_table),
    url(r'^request_service/', views.request_service),
]