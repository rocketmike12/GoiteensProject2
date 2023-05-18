import django_filters

from services.products_module.models import UserHistoryUnit


class UserHistoryUnitFilter(django_filters.FilterSet):
    user__username = django_filters.CharFilter(lookup_expr='icontains')
    calculator = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = UserHistoryUnit
        fields = ['calculator', 'user']

