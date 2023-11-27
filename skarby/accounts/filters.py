from accounts.models import Account
from django_filters import rest_framework as filter


class CategoryFilter(filter.BaseInFilter, filter.CharFilter):
    pass


class AccountFilter(filter.FilterSet):
    category = CategoryFilter(field_name='category__name', lookup_expr='in')

    class Meta:
        model = Account
        fields = ['category']

