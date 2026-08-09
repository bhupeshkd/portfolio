from django.http import Http404
from django.shortcuts import render


class Custom404Middleware:
    """Middleware to render custom 404 page even when DEBUG=True."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, Http404):
            return render(request, '404.html', status=404)
        return None