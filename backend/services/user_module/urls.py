from django.urls import path

from services.user_module import views as user_views

urlpatterns = [
    path('registration', user_views.registration, name='registration'),
]
