from django.urls import path, include
from services.products_module.views import index, basic_calculator, get_my_history, circle_area, square_area, triangle_area, premium

urlpatterns = [
    path('', index, name='index'),
    path('basic_calculator', basic_calculator, name='basic_calculator'),
    path('circle_area', circle_area, name='circle_area'),
    path('square_area', square_area, name='square_area'),
    path('triangle_area', triangle_area, name='triangle_area'),
    path('history', get_my_history, name='history'),
    path('premium', premium, name='premium'),
]
