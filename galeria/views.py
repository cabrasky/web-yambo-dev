from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImageForm
from django.shortcuts import redirect
from .models import Imagen, Actividad, Año, Grupo
from django.template import loader
import os

def grupo(request, grupo_de_edad):
    grupos = Grupo.objects.filter(año=Año.objects.last(), nombre=grupo_de_edad)
    grupo = grupos[0]
    actividades = Actividad.objects.filter(grupo=grupo).order_by('-dia')
    for i in range(len(actividades)):
        actividades[i].imagenList = []
        actividades[i].imagenList = actividades[i].imagen_set.all()
    

    template = loader.get_template('galeria/principal.html')
    context = {
        'grupo': grupo,
        'actividades': actividades
    }
    return HttpResponse(template.render(context, request))

def upload(request):
    if request.method == 'POST':
        form_p = ImageForm(request.POST)
        grupos = form_p.data.getlist("Grupos")
        print(grupos)
        for grupo in grupos:
            print(form_p.data.get("Fecha"))
            grupoN = Grupo.objects.get(id=grupo)
            a = Actividad.objects.create(dia=form_p.data.get("Fecha"))
            intI = 0
            for img in request.FILES.getlist('images'):
                path = os.path.join("galeria" ,Año.objects.last().__str__(), grupoN.nombre, form_p.data.get("Fecha"), intI.__str__ () + os.path.splitext(img.name)[1])
                i = Imagen.objects.create(path=path)
                i.img = img
                i.actividad = a
                i.save()
                intI += 1
            a.grupo = grupoN
            a.save()

        return redirect('/')

    form = ImageForm()

    context = {'form': form}

    return render(request, 'galeria/subir_fotos.html', context)