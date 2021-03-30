from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilterSet(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateTimeFromToRangeFilter()
    status = filters.ModelMultipleChoiceFilter(field_name='status', to_field_name='status', queryset=Advertisement.objects.all())

    class Meta:
        model = Advertisement
        fields = ('created_at', 'status', )
