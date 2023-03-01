from django.shortcuts import render,redirect
from django.core.exceptions import  ObjectDoesNotExist
from .forms import AutorForms
from .models import Autor

# Create your views here.
def Home(request):
    return render(request,'index.html')

def crearAutor(request):
    if request.method == 'POST':
        nom = request.POST.get('nombre')
        ape = request.POST.get('apellidos')
        nacio = request.POST.get('nacionalidad')
        desc = request.POST.get('descripcion')
        autor = Autor(nombre = nom, apellidos = ape, nacionalidad = nacio, descripcion = desc)
        autor.save()
        return redirect('index')
    #else:
        #autor_form = AutorForms()
    return render(request,'libro/crear_autor.html')


def listarAutor(request):
    autores = Autor.objects.filter(estado = True)
    return render(request,'libro/listar_autor.html',{'autores':autores})

def editarAutor(request,id):
    autor_form = None
    error = None
    try:
        autor = Autor.objects.get(id = id)
        if request.method == 'GET':
            autor_form = AutorForms(instance = autor)
        else:
            autor_form = AutorForms(request.POST, instance = autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e
    return render(request,'libro/crear_autor.html',{'autor_form':autor_form,'error':error})

def eliminarAutor(request,id):
    autor = Autor.objects.get(id = id)
    autor.estado = False
    autor.save()
    return redirect('libro:listar_autor')

