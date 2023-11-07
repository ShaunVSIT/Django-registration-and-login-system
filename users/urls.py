from django.urls import path
from .views import home, search_view, search_results

urlpatterns = [
    path('', search_view, name='users-home'),
    path('search/', search_view, name='search-view'),
    path('results/', search_results, name='search-results'),
]
