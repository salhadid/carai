from django.urls import path
from .views import api_list_salesperson, api_show_salesperson, api_list_customers, api_show_customer

urlpatterns = [
    path("salespeople/", api_list_salesperson, name="api_list_salesperson"),
    path("salespeople/<int:pk>/", api_show_salesperson, name="api_show_salesperson"),
    path("customers/", api_list_customers, name="api_list_customers"),
    path("customers/<int:pk>/", api_show_customer, name="api_show_customer"),
]
