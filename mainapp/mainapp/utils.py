from django.contrib.auth.models import Group


def size_cart(request):
    bolsa = request.session.get('bolsa', [])
    size_cart = len(bolsa)
    context = {
        'size_cart': size_cart
    }
    return context