from django.urls import path, include
from services.products_module.views import index, basic_calculator

urlpatterns = [
    path('', index, name='index'),
    path('basic_calculator', basic_calculator, name='basic_calculator'),
]
