from django.conf.urls import url
from django.contrib import admin
from rest_api_app import views

urlpatterns = [
    url(r"^$", views.api_root),
    url(r"^admin/", admin.site.urls),
    url(r"^login/", views.login),
    url(r"^logout/", views.logout),
    url(r"^register/", views.register),

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
    url(r"^get_user_info", views.get_user_info),
    url(r"^get_all_users/", views.get_all_users),
    url(r"^get_table/", views.get_table),

    url(r"^create_test_server/", views.create_test_server),
]
