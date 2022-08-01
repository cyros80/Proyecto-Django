from tkinter import INSERT
from urllib import request
from django.shortcuts import redirect, render
from .models import Alumnos, Comentarios ,Archivos
from .forms import ComentarioContactoForm, RegistrosForm, FormArchivos
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404
from django.contrib import messages

import datetime
# Create your views here.

def registros(request):
    alumnos= Alumnos.objects.all()
    
    return render(request, "registros/principal.html", {'alumnos': alumnos})


def consultar1(request):
    alumnos= Alumnos.objects.filter(carrera="TI")
    
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar2(request):
    alumnos= Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    
    return render(request, "registros/consultas.html", {'alumnos': alumnos})       

def consultar3(request):
    alumnos= Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "image")
    
    return render(request, "registros/consultas.html", {'alumnos': alumnos})     

def consultar4(request):
    alumnos= Alumnos.objects.filter(turno__contains="Vesp")
    
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar5(request):
    alumnos= Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
    
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar6(request):
   fechaInicio= datetime.date(2022, 7, 1)
   fechaFin = datetime.date(2022, 7, 13)
   alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    
   return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar7(request):
   alumnos=Alumnos.objects.filter(comentarios__coment__contains='Hola')
    
   return render(request, "registros/consultas.html", {'alumnos': alumnos})                      

def eliminarRegistro(request,matricula,
       confirmacion = 'registros/confirmEliminacion.html'):
       registro = get_object_or_404(Alumnos, matricula = matricula)
       if request.method=='POST':
             registro.delete()
             registros=Alumnos.objects.all()
             return render (request, "registros/principal.html", {'alumnos':registros})

       return render(request, confirmacion,{'object':confirmacion})    


def editarRegistro(request,matricula):
    registro=Alumnos.objects.get(matricula=matricula)
    return render(request,"registros/editarRegistro.html",{'registro':registro})

def consultarEditarRegistro(request,matricula):
    registro= get_object_or_404(Alumnos,matricula=matricula)
    form =RegistrosForm(request.POST, instance=registro)

    if form.is_valid():
          form.save()
          registros=Alumnos.objects.all()
          return render(request,"registros/principal.html",{'alumnos':registros})

    return render(request,"registros/editarRegistro.html",{'registro':registro})    



def contactocom(request):
    comentarios=ComentarioContacto.objects.all()

    return render(request, "registros/vistaContacto.html", {'comentarios':comentarios})    


def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            comentarios=ComentarioContacto.objects.all()
            return render (request, "registros/vistaContacto.html", {'comentarios':comentarios})
    form= ComentarioContactoForm()

    return render(request, 'registros/contacto.html', {'form':form}) 


def contacto(request):
    return render(request,"registros/contacto.html")

def eliminarComentarioContacto(request,id,
       confirmacion = 'registros/confirmarEliminacion.html'):
       comentario = get_object_or_404(ComentarioContacto, id = id)
       if request.method=='POST':
             comentario.delete()
             comentarios=ComentarioContacto.objects.all()
             return render (request, "registros/vistaContacto.html", {'comentarios':comentarios})

       return render(request, confirmacion,{'object':comentario})



def editarComentario(request,id):
    comentario=ComentarioContacto.objects.get(id=id)

    return render(request,"registros/editarComentario.html",{'comentario':comentario})

def consultarEditarComentario(request,id):
    comentario= get_object_or_404(ComentarioContacto,id=id)
    form =ComentarioContactoForm(request.POST, instance=comentario)

    if form.is_valid():
          form.save()
          comentarios=ComentarioContacto.objects.all()
          return render(request,"registros/vistaContacto.html",{'comentarios':comentarios})

    return render(request,"registros/editarComentario.html",{'comentario':comentario})  

def archivos(request):
    if request.method =='POST':
        form=FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo=request.POST['titulo']
            archivo=request.FILES['archivo']
            insert=Archivos(titulo=titulo, archivo=archivo)
            insert.save()
            return render (request, "registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")


    else:
        return render(request,"registros/archivos.html",{'archivo':Archivos})
    

def consultasSQL(request):
    alumnos=Alumnos.objects.raw('SELECT matricula,nombre,carrera,turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')

    return render(request, "registros/consultas.html", {'alumnos':alumnos})    


def seguridad(request, nombre=None):
    nombre= request.GET.get('nombre')
    return render(request, "registros/seguridad.html", {'nombre':nombre})    