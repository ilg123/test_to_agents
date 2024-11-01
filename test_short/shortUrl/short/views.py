from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ShortURL
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def shorten_url(request):
    if request.method == "POST":
        original_url = request.POST.get('original_url')
        if not original_url:
            return HttpResponse("Original URL is required", status=400)

        url, created = ShortURL.objects.get_or_create(original_url=original_url)
        short_url = request.build_absolute_uri(f'/{url.short_url}')
        return render(request, 'short/home.html', {'short_url': short_url})
    else:
        return render(request, 'short/home.html')

def redirect_url(request, short_url):
    url = get_object_or_404(ShortURL, short_url=short_url)
    return redirect(url.original_url)
