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
