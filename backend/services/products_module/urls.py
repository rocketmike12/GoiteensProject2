from django.urls import path, include
from services.products_module.views import index, basic_calculator, get_my_history

urlpatterns = [
    path('', index, name='index'),
    path('basic_calculator', basic_calculator, name='basic_calculator'),
    path('history', get_my_history, name='history'),
]
