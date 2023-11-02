#para trabajar con formularios crear un archivo forms.py en mi app y luego la importo a la view

from django import forms
from .models import Favoritos #importo el modelo para el modelform

#tradicional bien, se construye cada campo a usar
class FavoritoForm(forms.Form):
    nombre = forms.CharField()
    url = forms.URLField()

#usando el modelo de datos, bonito, se mapea solo
class FavoritoModelForm(forms.ModelForm):
    class Meta: #creo una clase meta dentro del modelform para indicar los datos
        model = Favoritos #selecciono el modelo
        fields = '__all__' #indico los campos, puede ser todos o uno por uno en una lista ['nombre','url']