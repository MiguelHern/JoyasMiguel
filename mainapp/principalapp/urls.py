from django.urls import path

from .views import home, ingresar, exit, marcas, IrProducto, AgregarCarrito, carrito, eliminarCarrito, IrMarcas, signin, \
    buscador, Payment

urlpatterns = [
    path('ingresar/', ingresar, name='ingresar'),
    path('registro/', signin, name='registro'),
    path('logout/', exit, name='exit'),

    path('marcas/', marcas, name='marcas'),
    path('buscardor/', buscador, name='buscador'),

    path('', home, name='home'),
    path('irProducto/<int:id>', IrProducto, name='irProducto'),
    path('irMarcas/<int:id>', IrMarcas, name='irMarcas'),

    path('AgregarCarrito/<int:id>', AgregarCarrito),
    path('carrito', carrito, name='carrito'),
    path('eliminar_carrito/<int:id>', eliminarCarrito),

    path('SeleccionarDireccion/', Payment, name='Payment'),


]