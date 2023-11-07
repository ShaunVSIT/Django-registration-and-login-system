from django.urls import path
from .views import home, profile, RegisterView, search_view, search_results

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('search/', search_view, name='search-view'),
    path('results/', search_results, name='search-results'),
]
