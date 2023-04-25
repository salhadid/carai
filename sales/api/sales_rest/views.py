from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from common.json import ModelEncoder
from .models import Salesperson, Sale, Customer, AutomobileVO


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
        "id",
    ]

    def get_extra_data(self, o):
        return {
            "automobile": o.automobile.vin,
            "salesperson": {
                "first_name": o.salesperson.first_name,
                "last_name": o.salesperson.last_name,
                "employee_id": o.salesperson.employee_id,
            },
            "customer": {
                "first_name": o.customer.first_name,
                "last_name": o.customer.last_name,
                "address": o.customer.address,
                "phone_number": o.customer.phone_number,
            },
            "price": str(o.price),
        }


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
        count, _ = get_object_or_404(Salesperson, employee_id=pk).delete()
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


@require_http_methods(["GET", "POST"])
def api_list_sales(request, automobile_vo_vin=None):
    if request.method == "GET":
        if automobile_vo_vin is not None:
            sales = Sale.objects.filter(automobile=automobile_vo_vin)
        else:
            sales = Sale.objects.all()
        return JsonResponse(
            {"sales": sales},
            encoder=SaleListEncoder,
        )
    else:
        content = json.loads(request.body)
        try:
            automobile_vin = content["automobile"]
            automobile = AutomobileVO.objects.get(vin=automobile_vin)
            content["automobile"] = automobile
        except AutomobileVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid automobile vin"},
                status=400,
            )
        try:
            salesperson = Salesperson.objects.get(employee_id=content["salesperson"])
            content["salesperson"] = salesperson
        except Salesperson.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid salesperson ID"},
                status=400,
            )

        try:
            customer = Customer.objects.get(id=content["customer"])
            content["customer"] = customer
        except Customer.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid customer ID"},
                status=400,
            )
        sale = Sale.objects.create(**content)
        return JsonResponse(
            sale,
            encoder=SaleListEncoder,
            safe=False,
        )


@require_http_methods(["GET", "DELETE"])
def api_show_sale(request, pk):
    if request.method == "GET":
        sale = Sale.objects.get(id=pk)
        return JsonResponse(
            sale,
            encoder=SaleListEncoder,
            safe=False,
        )
    else:
        count, _ = Sale.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})
