from django.shortcuts import render

def search_form(request):
    """Search form view."""
    return render(request, 'webApp/search.html')

