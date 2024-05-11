from django.urls import path

from .views import home, ingresar, exit, marcas, IrProducto, AgregarCarrito, carrito, eliminarCarrito

urlpatterns = [
    path('', home, name='home'),
    path('ingresar/', ingresar, name='ingresar'),
    path('logout/', exit, name='exit'),
    path('marcas/', marcas, name='marcas'),
    path('irProducto/<int:id>', IrProducto, name='irProducto'),
    path('AgregarCarrito/<int:id>', AgregarCarrito),
    path('carrito', carrito, name='carrito'),
    path('eliminar_carrito/<int:id>', eliminarCarrito),
]