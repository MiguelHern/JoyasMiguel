from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Productos)

admin.site.register(Marcas)

admin.site.register(Proveedores)