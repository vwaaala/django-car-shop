import django_filters
from .models import Item


class ItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Item
        fields = ('group', 'category', 'brand', 'model')
