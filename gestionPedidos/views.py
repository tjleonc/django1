from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    if request.GET['prd']:    
        #mensaje = 'Articulo buscado: %r'%request.GET['prd'] # request.GET['prd'] es el valor del campo de texto en el formulario de busqueda_productos.html
        producto = request.GET['prd']

        if len(producto) > 20:
            return HttpResponse("Texto de busqueda demasiado largo")
        else:
            articulos = Articulos.objects.filter(nombre__icontains=producto) # __icontains es un filtro que busca el valor de producto en la columna nombre de la tabla Articulos
        return render(request, "resultados_busqueda.html", {"articulos": articulos, "query": producto}) # La variable articulos es un diccionario que contiene los articulos que coinciden con la busqueda y la variable query contiene el valor de producto, lo que hacemos es pasarle estos valores a la plantilla resultados_busqueda.html para que los muestre en la pagina
    
    else:
        mensaje = 'No has introducido ningun articulo'
    return HttpResponse(mensaje)

def contacto(request):

    if request.method == "POST":
        return render(request,"gracias.html")



    return render(request, "contacto.html")