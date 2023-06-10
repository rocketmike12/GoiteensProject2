from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from services.products_module.models import Product, UserHistoryUnit
from services.user_module.models import User
from django.core.paginator import Paginator
from rest_framework import status
from django.contrib.auth.decorators import login_required
from math import sqrt, sin, cos, tan
import datetime

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

    file = request.user.files()
    context = {'products': page_obj, 'pages_count': paginator.num_pages, 'page_number': page_number, 'file': file}
    return render(request, 'index.html', context)


@login_required
def get_my_history(request):
    history = UserHistoryUnit.objects.filter(user=request.user).order_by('-id')
    paginator = Paginator(history, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    file = request.user.files()
    context = {'history': page_obj, 'pages_count': paginator.num_pages, 'page_number': page_number, 'file': file}

    return render(request, 'history.html', context)


def basic_calculator(request):
    file = request.user.files()
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        if 'add' in request.POST:
            result = float(num1) + float(num2)
            UserHistoryUnit.objects.create(user=request.user, input=f"{num1} + {num2}", result=result)
            return render(request, 'basic_calculator.html', {'result': result, 'file': file})

        if 'sub' in request.POST:
            result = float(num1) - float(num2)
            UserHistoryUnit.objects.create(user=request.user, input=f"{num1} - {num2}", result=result)
            return render(request, 'basic_calculator.html', {'result': result, 'file': file})

        if 'div' in request.POST:
            result = float(num1) / float(num2)
            UserHistoryUnit.objects.create(user=request.user, input=f"{num1} / {num2}", result=result)
            return render(request, 'basic_calculator.html', {'result': result, 'file': file})

        if 'mul' in request.POST:
            result = float(num1) * float(num2)
            UserHistoryUnit.objects.create(user=request.user, input=f"{num1} * {num2}", result=result)
            return render(request, 'basic_calculator.html', {'result': result, 'file': file})

    return render(request, 'basic_calculator.html', {'file': file})


def circle_area(request):
    file = request.user.files()
    if request.method == 'POST':
        radius = request.POST['radius']
        if 'calculate' in request.POST:
            result = 3.141 * (float(radius) ** 2)
            UserHistoryUnit.objects.create(user=request.user, input=f"Area of circle with radius {radius}", result=result)
            return render(request, 'circle_area.html', {'result': result, 'file': file})

    return render(request, 'circle_area.html', {'file': file})


def square_area(request):
    file = request.user.files()
    if request.method == 'POST':
        side_length = request.POST['side_length']
        if 'calculate' in request.POST:
            result = float(side_length) ** 2
            UserHistoryUnit.objects.create(user=request.user, input=f"Area of square with side length {side_length}", result=result)
            return render(request, 'square_area.html', {'result': result, 'file': file})

    return render(request, 'square_area.html', {'file': file})


def triangle_area(request):
    file = request.user.files()
    if request.user.is_premium:
        if request.method == 'POST':
            a = request.POST['a']
            b = request.POST['b']
            c = request.POST['c']
            if 'calculate' in request.POST:
                a = float(a)
                b = float(b)
                c = float(c)
                s = (a + b + c) / 2
                result = sqrt(s * (s - a) * (s - b) * (s - c))
                UserHistoryUnit.objects.create(user=request.user, input=f"Area of triangle with:\n"
                                                                        f"Side A: {a} cm;\n"
                                                                        f"Side B: {b} cm;\n"
                                                                        f"Side C: {c} cm", result=result)
                return render(request, 'triangle_area.html', {'result': result, 'file': file})
        return render(request, 'triangle_area.html', {'file': file})
    else:
        return redirect('premium')


def premium(request):
    file = request.user.files()
    if request.method == 'POST':
        user = request.user
        if 'forever' in request.POST:
            user.is_premium = True
            user.save()
            return redirect('index')

    return render(request, 'premium.html', {'file': file})

