from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class clientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","email","telefono") # Campos que se mostrarán en la lista de registros de la interfaz de administración
    search_fields=("nombre","telefono") # Campos por los que se puede buscar en la interfaz de administración

class articulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",) # Campos por los que se puede filtrar en la interfaz de administración
    list_display=("nombre","seccion","precio") # Campos que se mostrarán en la lista de registros de la interfaz de administración
    search_fields=("nombre","seccion") # Campos por los que se puede buscar en la interfaz de administración

class pedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha","entregado") # Campos que se mostrarán en la lista de registros de la interfaz de administración
    list_filter=("fecha",) # Campos por los que se puede filtrar en la interfaz de administración
    date_hierarchy="fecha" # Campo por el que se puede filtrar por fechas en la interfaz de administración

admin.site.register(Clientes, clientesAdmin)
admin.site.register(Articulos, articulosAdmin)
admin.site.register(Pedidos, pedidosAdmin)