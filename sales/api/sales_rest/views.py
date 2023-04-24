from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from common.json import ModelEncoder
from .models import Salesperson, Sale, Customer


class SalesPersonListEncoder(ModelEncoder):
    model = Salesperson
    properties = [
        "first_name",
        "last_name",
        "employee_id",
    ]


class CustomerListEncoder(ModelEncoder):
    model = Customer
    properties = [
        "id",
        "first_name",
        "last_name",
        "address",
        "phone_number",
    ]


class SaleListEncoder(ModelEncoder):
    model = Sale
    properties = [
        "salesperson",
        "customer",
        "price",
    ]

    def get_extra_data(self, o):
        return {"vin": o.automobile.vin}


@require_http_methods(["GET", "POST"])
def api_list_salesperson(request):
    if request.method == "GET":
        salespeople = Salesperson.objects.all()
        return JsonResponse(
            {"salespeople": salespeople},
            encoder=SalesPersonListEncoder,
        )
    else:
        content = json.loads(request.body)
        salesperson = Salesperson.objects.create(**content)
        return JsonResponse(
            salesperson,
            encoder=SalesPersonListEncoder,
            safe=False,
        )


@require_http_methods(["DELETE", "GET"])
def api_show_salesperson(request, pk):
    if request.method == "GET":
        salesperson = Salesperson.objects.get(employee_id=pk)
        return JsonResponse(
            salesperson,
            encoder=SalesPersonListEncoder,
            safe=False,
        )
    else:
        count, _ = Salesperson.objects.filter(employee_id=pk).delete()
        return JsonResponse({"deleted": count > 0})


@require_http_methods(["GET", "POST"])
def api_list_customers(request):
    if request.method == "GET":
        customers = Customer.objects.all()
        return JsonResponse(
            {"customers": customers},
            encoder=CustomerListEncoder,
        )
    else:
        content = json.loads(request.body)
        customer = Customer.objects.create(**content)
        return JsonResponse(
            customer,
            encoder=CustomerListEncoder,
            safe=False,
        )


@require_http_methods(["DELETE", "GET"])
def api_show_customer(request, pk):
    if request.method == "GET":
        customer = Customer.objects.get(id=pk)
        return JsonResponse(
            customer,
            encoder=CustomerListEncoder,
            safe=False,
        )
    else:
        count, _ = Customer.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})


# @require_http_methods(["GET", "POST"])
# def api_list_sales(request):
#     if request.method == "GET":
#         customers = Customer.objects.all()
#         return JsonResponse(
#             {"customers": customers},
#             encoder=CustomerListEncoder,
#         )
#     else:
#         content = json.loads(request.body)
#         customer = Customer.objects.create(**content)
#         return JsonResponse(
#             customer,
#             encoder=CustomerListEncoder,
#             safe=False,
#         )


# @require_http_methods(["DELETE", "GET"])
# def api_show_customer(request, pk):
#     if request.method == "GET":
#         customer = Customer.objects.get(id=pk)
#         return JsonResponse(
#             customer,
#             encoder=CustomerListEncoder,
#             safe=False,
#         )
#     else:
#         count, _ = Customer.objects.filter(id=pk).delete()
#         return JsonResponse({"deleted": count > 0})
