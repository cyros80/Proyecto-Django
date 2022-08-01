from dataclasses import field, fields
from pyexpat import model
from re import template
from tkinter import Widget
from django import forms
from .models import Alumnos, ComentarioContacto
from .models import Archivos
from django.forms import ModelForm, ClearableFileInput

class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['usuario', 'mensaje']

class RegistrosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['nombre','carrera','turno']

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear='<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label>%(clear)s'

class FormArchivos(ModelForm):
    class Meta:
        model=Archivos
        fields=('titulo','archivo')
        widgets={
            'archivo':CustomClearableFileInput
        }                    