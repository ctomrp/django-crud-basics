from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Favoritos #importo el modelo para crear instancias desde un formulario
from .forms import FavoritoForm, FavoritoModelForm

# Create your views here.
#las vistas son funciones comunes de python que reciben un parametro (request por convención) y retorna un response, pero con render
def index_favoritos(request):
    favoritos_lista = Favoritos.objects.all()
    context = {
        'favoritos_lista':favoritos_lista
    }

    # for fav in favoritos_lista:
    #     print(fav.name)
    #     print(fav.url)

    # print(favoritos_lista.query)
    #return render(request, 'index.html') #si es el index de la app poner 'favoritos/index.html', sino tomará el general
    return render(request, 'favoritos/lista.html', context)

def crear_favoritos(request):
    #form = FavoritoForm() #para la forma tradicional
    form = FavoritoModelForm()

    if request.method == 'POST':
        form = FavoritoModelForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            print(form.errors)

        '''
        # nombre = request.POST['nombre']
        # url = request.POST['url']
        form = FavoritoForm(request.POST) #asi mapea solo
        if form.is_valid():
            nombre = form.cleaned_data['nombre'] #indicar el name del template
            url = form.cleaned_data['url']
            Favoritos.objects.create(name=nombre, url=url)
        else:
            print(form.errors)
        '''

    context = { #el contexto es un diccionario para mapear el form del template y completar el form de forms
        'form': form,
        'titulo': 'Crear favorito'
    }

        #A LO CAVERNICOLA
        # favorito = Favoritos()
        # favorito.name = nombre
        # favorito.url = url
        # favorito.save()

    return render(request, 'favoritos/crear.html', context) #tercer parametro es el contexto


def borrar_favoritos(request, pk):
    Favoritos.objects.get(pk=pk).delete()
    # return index_favoritos(request)
    # return redirect(reverse('favoritos:borrar'), kwargs={'pk':pk}) #reverse cuando hay argumentos en la url
    return redirect('favoritos:index')


def detalle_favoritos(request, pk):
    favorito = Favoritos.objects.get(pk=pk)
    return render(request, 'favoritos/detalle.html', context={'object': favorito})

def actualizar_favoritos(request, pk):
    favorito = Favoritos.objects.get(pk=pk)
    form = FavoritoModelForm(instance=favorito)
    if request.method == 'POST':
        form = FavoritoModelForm(request.POST, instance=favorito)
        if form.is_valid():
            form.save()
        else:
            print(form.errors())

    context = {
        'form': form,
        'titulo': 'Actualizar favorito'
    }

    return render(request, 'favoritos/crear.html', context)