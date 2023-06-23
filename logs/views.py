#importing all the required libraries
from django.shortcuts import render
import pandas as pd
from logs.models import restaurant


#searching for the dish in the database
def home(request):
    query = request.GET.get('query', '')  # Get the search query from the request
    results = restaurant.objects.filter(items__icontains=query)  # Perform the search query

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'home.html', context)
