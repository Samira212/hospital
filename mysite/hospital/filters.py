from django_filters.rest_framework import FilterSet
from .models import UserProfile

class UserProfileFilter(FilterSet):
    class Meta:
        model = UserProfile
        fields = {
            'category': ['exact'],
            'price': ['gt', 'lt']
        }