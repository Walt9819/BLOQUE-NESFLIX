from django import forms
from STREAMING.models import Pelis

class FormularioPelis(forms.ModelForm):
    class Meta:
        model = Pelis
        fields = ['titulo', 'sinopsis', 'director', 'fecha_lanzamiento', 'poster']
        labels = {
            'titulo': 'Título:',
            'sinopsis': 'Sinopsis:',
            'director': 'Director:',
            'fecha_lanzamiento': 'Fecha de lanzamiento de la película:',
            'poster': 'Poster de la película:',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'sinopsis': forms.Textarea(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_lanzamiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'yyyy-mm-dd'}),
            'poster': forms.FileInput(attrs={'class': 'form-control'}),
        }