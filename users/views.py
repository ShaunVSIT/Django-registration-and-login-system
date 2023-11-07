from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.html import escape

from .forms import SearchForm


def home(request):
    return render(request, 'users/home.html')

def search_view(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data['search']
            # No need to escape here as Django templates escape variables by default
            search_results_url = reverse('search-results') + '?search_query=' + search_term
            return HttpResponseRedirect(search_results_url)
        else:
            # If the form is not valid, it could be because of a ValidationError
            # Handle the form errors here
            # For example, you might want to return to the same page with the form errors
            # return render(request, 'search/search.html', {'form': form})
            messages.warning(request, 'Potential XSS or SQL injection detected.')
            form = SearchForm()  # Re-instantiate the form without the POST data to clear it
    else:
        form = SearchForm()
    return render(request, 'search/search.html', {'form': form})

def search_results(request):
    # No need to accept 'search_query' as an argument since it's being passed as a query parameter
    search_query = request.GET.get('search_query', '')  # This will get the search term from the query string
    # Now you can use 'search_query' in your context or for further processing
    return render(request, 'search/search_results.html', {'search_query': search_query})
