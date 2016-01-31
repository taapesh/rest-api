from django.conf.urls import patterns, url, include
from django.contrib import admin
from rest_api_app import views

urlpatterns = patterns("",
    url(r"^auth/", include("djoser.urls.authtoken")),
)

urlpatterns += [
    url(r"^admin/", admin.site.urls),

    url(r"^create_table/", views.create_or_join_table),
    url(r"^all_tables/", views.get_all_tables),
    url(r"^server_tables/", views.get_server_tables),
    url(r"^delete_table/", views.delete_table),
    url(r"^users_at_table/", views.get_users_at_table),
    url(r"^request_service/", views.request_service),
    url(r"^serve_request/", views.serve_request),
    url(r"^check_for_request/", views.has_request),
    url(r"^place_order/", views.place_order),
    url(r"^get_table_orders/", views.get_table_orders),
    url(r"^finish_and_pay/", views.finish_and_pay),
    url(r"^get_receipts/", views.get_receipts),
    url(r"^get_orders/", views.get_orders),
]
