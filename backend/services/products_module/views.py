from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from services.products_module.models import Product
from django.core.paginator import Paginator
from rest_framework import status

from django.template.defaulttags import register


@register.filter
def get_range(value):
    return range(1, value + 1)

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect('auth')

    products = Product.objects.all()
    paginator = Paginator(products, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'products': page_obj, 'pages_count': paginator.num_pages, 'page_number': page_number}
    return render(request, 'index.html', context)


def add(num1, num2):
    result = int(num1) + int(num2)
    return result


def subtract(num1, num2):
    result = int(num1) - int(num2)
    return result


def divide(num1, num2):
    result = int(num1) / int(num2)
    return result


def multiply(num1, num2):
    result = int(num1) * int(num2)
    return result


def basic_calculator(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        if 'add' in request.POST:
            result = add(num1, num2)
            return render(request, 'basic_calculator.html', {'result': result})

        if 'sub' in request.POST:
            result = subtract(num1, num2)
            return render(request, 'basic_calculator.html', {'result': result})

        if 'div' in request.POST:
            result = divide(num1, num2)
            return render(request, 'basic_calculator.html', {'result': result})

        if 'mul' in request.POST:
            result = multiply(num1, num2)
            return render(request, 'basic_calculator.html', {'result': result})
    return render(request, 'basic_calculator.html')