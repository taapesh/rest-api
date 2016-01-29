from django.conf.urls import patterns, url, include
from django.contrib import admin
from rest_api_app import views

urlpatterns = patterns('',
    url(r'^auth/', include('djoser.urls.authtoken')),
)

urlpatterns += [
    url(r'^admin/', admin.site.urls),

    url(r'^createtable/', views.create_or_join_table),
    url(r'^alltables/', views.get_all_tables),
    url(r'^deletetable/', views.delete_table),
    url(r'^usersattable/', views.get_users_at_table),
]