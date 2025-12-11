from django.http import HttpResponseBadRequest

def ajax_required(func):
    def wrap(request, *args, **kwargs):
        # Check AJAX header manually
        if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
            return HttpResponseBadRequest('Bad request - Not AJAX')
        return func(request, *args, **kwargs)

    wrap.__doc__ = func.__doc__
    wrap.__name__ = func.__name__
    return wrap
