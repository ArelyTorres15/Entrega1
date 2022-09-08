from django.shortcuts import render
from .models import *
from django.http import HttpResponse

from AppCoder.forms import *
# Create your views here.

def ropa(request):

    
    descripcion = request.POST.get("descripcion")
    precio = request.POST.get("precio")
    ropa = Ropa(descripcion=descripcion, precio=precio)
    ropa.save()
    ropa=Ropa(descripcion="vestido", precio=650)
    print("primer articulo")
    ropa.save()
    
    texto=f"primer articulo"
    return HttpResponse(texto)

def inicio(request):
    return render (request, "AppCoder/inicio.html")

def ropa(request):
    return render (request, "AppCoder/ropa.html")


def clientes(request):
    return render (request, "AppCoder/clientes.html")

def staff(request):
    return render (request, "AppCoder/staff.html")

def envios(request):
    return render (request, "AppCoder/envios.html")


def ropa(request):
    if request.method=="POST":
        form=RopaForm(request.POST)
        print("-------------------------------")
        print(form)
        print("-------------------------------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            descripcion=informacion["descripcion"]
            precio=informacion["precio"]
            ropa=Ropa(descripcion=descripcion, precio=precio)
            ropa.save()
            return render (request, "AppCoder/inicio.html")


    else:
        formulario=RopaForm()
        return render (request, "AppCoder/ropa.html", {"formulario":formulario})


def staffFormulario(request):

    if request.method=="POST":
        form= StaffForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            apellido= info["apellido"]
            email= info["email"]
            profesion= info["profesion"]
            staff= Staff(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            staff.save()
            return render (request, "Appcoder/inicio.html", {"mensaje":"Staff creado"})
    else:
        form= StaffForm()
    return render(request, "Appcoder/staffForm.html", {"formulario":form})



##........................

def busquedaPrecio(request):
    return render(request, "Appcoder/busquedaPrecio.html")

def buscar(request):
    if request.GET["precio"]:
       # precio=request.GET["precio"]
       if 'precio' in request.GET:
        ropa=Ropa.objects.filter(precio= precio)
        return render(request, "Appcoder/resultadosBusqueda.html", {"ropa":ropa})
    else:
        return render(request, "Appcoder/busquedaPrecio.html", {"mensaje":"Ingresa un precio"})
    
    return HttpResponse(respuesta)



    
    








