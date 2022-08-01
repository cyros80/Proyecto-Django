from unicodedata import name
from django.contrib import admin
from .models import Alumnos
from .models import Comentarios
from .models import ComentarioContacto

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields= ('created', 'update')
    list_display= ('matricula', 'nombre', 'carrera', 'turno','created')
    search_fields= ('image', 'matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy= 'created'
    list_filter= ('carrera', 'turno')
    list_per_page=2
    list_display_links=('matricula', 'nombre')
    list_editable=('turno',)

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Usuarios").exists():

              return('matricula','carrera','turno')
        else:
              return('created', 'update')    

class administraComentarios(admin.ModelAdmin):
    list_display= ('id', 'coment')
    search_fields= ('id', 'created')
    date_hierarchy= 'created'
    readonly_fields= ('created', 'id')

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display=('id', 'mensaje')
    search_fields= ('id', 'created')
    date_hierarchy= 'created'
    readonly_fields= ('created', 'id')



admin.site.register(ComentarioContacto, AdministrarComentariosContacto)

admin.site.register(Alumnos, AdministrarModelo)

admin.site.register(Comentarios, administraComentarios)