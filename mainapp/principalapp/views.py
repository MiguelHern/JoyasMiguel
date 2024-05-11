from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404

from principalapp.models import Productos


# Create your views here.


def home(request):
    productos = Productos.objects.all()

    return render(request, 'home.html', {'productos': productos})


def ingresar(request):
    return render(request, 'ingreso/login.html')


def exit(request):
    logout(request)
    return redirect('home')

def marcas(request):
    return render(request, 'marcas.html')


def carrito(request):
    bolsa = request.session.get('bolsa',[])
    productos = Productos.objects.filter(id__in=bolsa)
    carrito={'productos':productos}
    return render(request, 'AgregarCarrito.html',carrito)


def IrProducto(request, id):
    producto = get_object_or_404(Productos, pk=id)
    return render(request, 'producto.html', {"producto": producto})

#carrito=bolsa y productoInfo = irProducto
def AgregarCarrito(request, id):
    bolsa = request.session.get('bolsa', [])
    bolsa.append(id)
    request.session['bolsa'] = bolsa
    return redirect('irProducto', id=id)





def eliminarCarrito(request, id):
    bolsa = request.session.get('bolsa', [])

    try:
        bolsa.remove(int(id))
        request.session['bolsa'] = bolsa
    except ValueError:
        pass  # Si el ID del producto no es válido, simplemente no hagas nada

    return redirect("carrito")
