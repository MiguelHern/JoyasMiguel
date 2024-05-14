from collections import Counter

from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404


from principalapp.models import Productos, Marcas

from mainapp.utils import size_cart

from principalapp.forms import RegistrationForm


# Create your views here.

def buscador(request):
    if request.method == 'POST':
        texto_busqueda = request.POST.get('buscador__productos')
        productos = Productos.objects.filter(nombre__icontains=texto_busqueda)
        cantidad = len(productos)
        marcas = Marcas.objects.values('nombre').distinct()
        context = size_cart(request)
        # Pasar el texto de búsqueda como contexto a la plantilla informacion
        return render(request, 'Buscador.html', {'productos': productos, 'cantidad': cantidad, 'texto_busqueda': texto_busqueda, 'marcas': marcas, **context})



def home(request):
    productos = Productos.objects.all()
    marcas = Marcas.objects.all()
    charm = Productos.objects.filter(categoria='charms')
    arete = Productos.objects.filter(categoria='aretes')
    anillo = Productos.objects.filter(categoria='anillos')
    brazalete = Productos.objects.filter(categoria='brazaletes')
    collar = Productos.objects.filter(categoria='collares')
    context = size_cart(request)
    return render(request, 'home.html', {'charm': charm, 'marcas': marcas, 'anillo': anillo, 'arete': arete, 'brazalete': brazalete, 'collar': collar,'productos': productos, **context})


def ingresar(request):
    return render(request, 'ingreso/login.html')


def signin(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'ingreso/registro.html', {'form': form})



def exit(request):
    logout(request)
    return redirect('home')


def marcas(request):
    marcas = Marcas.objects.all()
    context = size_cart(request)
    return render(request, 'marcas.html',{'marcas': marcas, **context})


def IrMarcas(request, id):
    marca = get_object_or_404(Marcas, pk=id)
    marcasa = Marcas.objects.all()
    productos = Productos.objects.all()
    context = size_cart(request)
    return render(request, 'marcaa.html', {'marcasa' : marcasa,'marca': marca,'productos': productos,**context})


def carrito(request):
    bolsa = request.session.get('bolsa', [])

    counter = Counter(bolsa)

    tamano = len(bolsa)

    productos = Productos.objects.filter(id__in=bolsa)

    # Iterar sobre todos los productos en el carrito y sumar sus precios
    subtotal = 0.0
    for producto_id in bolsa:
        producto = Productos.objects.get(id=producto_id)
        subtotal += float(producto.precio)

    total = subtotal+50

    # Obtener el tamaño del carrito contando la cantidad de elementos
    context = size_cart(request)

    contador_dict = dict(counter)

    return render(request, 'AgregarCarrito.html', {'productos': productos, 'total': total, 'subtotal': subtotal, 'contador_ids': contador_dict, 'tamano': tamano, **context})


def IrProducto(request, id):
    producto = get_object_or_404(Productos, pk=id)
    context = size_cart(request)
    return render(request, 'producto.html', {"producto": producto, **context})


#carrito=bolsa y productoInfo = irProducto
def AgregarCarrito(request, id):
    bolsa = request.session.get('bolsa', [])
    bolsa.append(id)
    request.session['bolsa'] = bolsa
    redirect_url = request.META.get('HTTP_REFERER')
    return redirect(redirect_url, id=id)



def eliminarCarrito(request, id):
    bolsa = request.session.get('bolsa', [])
    try:
        bolsa.remove(int(id))
        request.session['bolsa'] = bolsa
    except ValueError:
        pass  # Si el ID del producto no es válido, simplemente no hagas nada

    return redirect("carrito")


def Payment(request):
    bolsa = request.session.get('bolsa', [])

    tamano = len(bolsa)


    # Iterar sobre todos los productos en el carrito y sumar sus precios
    subtotal = 0.0
    for producto_id in bolsa:
        producto = Productos.objects.get(id=producto_id)
        subtotal += float(producto.precio)

    total = subtotal+50

    context = size_cart(request)


    return render(request, 'PaymentV.html', {'total': total, 'subtotal': subtotal, 'tamano': tamano, **context})
