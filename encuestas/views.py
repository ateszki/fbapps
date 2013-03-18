from django.forms.models import modelformset_factory
from django.template import Context, loader, RequestContext
from encuestas.models import Encuestas, Preguntas, Respuestas, EncuestasForm, PreguntasForm, RespuestasForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from copy import copy,deepcopy

# Create your views here.
@login_required

def index(request):
    #return HttpResponse("Bienvenido!")
    if Encuestas.objects.count() > 0 :
        e = Encuestas.objects.all()
        c = Context({
            'encuestas': e,
        })
    else:
        c = Context({
            'encuestas': '',
        })
    t = loader.get_template('encuestas/index.html')
    return HttpResponse(t.render(c))

def detail(request, encuesta_id):
    e = Encuestas.objects.get(pk=encuesta_id)
    if e.preguntas_set.count() > 0:
        preg = e.preguntas_set.all()
        #respuestas = preg.respuestas_set.all()
        c = Context({
            'encuesta': e,
            'preguntas': preg,
        })
    else:
        c = Context({
            'encuesta': e,
            'pregunta': '',
        })
        
    #t = loader.get_template('encuestas/preguntas.html')
    #return HttpResponse(t.render(c))
    return render_to_response("encuestas/preguntas.html", c,RequestContext(request)) 

def pregunta_mover(request,encuesta_id,pregunta_id,sentido):
    try:
        encuesta = Encuestas.objects.get(pk=encuesta_id)
        pregunta = encuesta.preguntas_set.get(pk=pregunta_id)
        encuesta.mover(pregunta,sentido)
        return HttpResponseRedirect("/encuestas/%s" % (encuesta_id))
    except ObjectDoesNotExist:
        raise Http404
    

def pregunta_delete(request, encuesta_id, pregunta_id = None):
    try:
        encuesta = Encuestas.objects.get(pk=encuesta_id)
        pregunta = encuesta.preguntas_set.get(pk=pregunta_id)
        pregunta.delete()
        return HttpResponseRedirect("/encuestas/%s" % (encuesta_id))
    except ObjectDoesNotExist:
        raise Http404

def pregunta(request, encuesta_id, pregunta_id = None, accion = None):
    try: 
        encuesta = Encuestas.objects.get(pk=encuesta_id)
        if pregunta_id is None:
            pregunta = Preguntas(encuesta=encuesta)
        else:
            pregunta = encuesta.preguntas_set.get(pk=pregunta_id) 

        if request.method == 'POST':
            form = PreguntasForm(request.POST, instance=pregunta)
            if form.is_valid():
                new_pregunta = form.save()
                return HttpResponseRedirect("/encuestas/%s" % (encuesta_id))
        else:
            if accion == 'duplicar':
                clon_pregunta = copy(pregunta)
                clon_respuestas = pregunta.respuestas_set.all()
                clon_pregunta.pregunta += ' - Duplicado'
                clon_pregunta.id = None
                clon_pregunta.save()
                
                for r in clon_respuestas:
                    r.id = None
                    r.pregunta = clon_pregunta
                    r.save()
                return HttpResponseRedirect("/encuestas/%s/%s" % (encuesta_id,clon_pregunta.id))

            form = PreguntasForm(instance=pregunta)
                    
            c = Context({
                'form': form,
            })
            c.update(csrf(request))
            
            return render_to_response("encuestas/edit_preguntas.html", c)    
    except ObjectDoesNotExist:
        raise Http404

def respuesta_delete(request, encuesta_id, pregunta_id, respuesta_id = None):
    try:
        encuesta = Encuestas.objects.get(pk=encuesta_id)
        pregunta = encuesta.preguntas_set.get(pk=pregunta_id)
        respuesta = pregunta.respuestas_set.get(pk=respuesta_id)
        respuesta.delete()
        return HttpResponseRedirect("/encuestas/%s" % (encuesta_id))
    except ObjectDoesNotExist:
        raise Http404

def respuesta(request, encuesta_id, pregunta_id, respuesta_id = None):
    try: 
        encuesta = Encuestas.objects.get(pk=encuesta_id)
        pregunta = encuesta.preguntas_set.get(pk=pregunta_id)
        if respuesta_id is None:
            respuesta = Respuestas(pregunta=pregunta)
        else:
            respuesta = pregunta.respuestas_set.get(pk=respuesta_id) 
        if request.method == 'POST':
            form = RespuestasForm(request.POST, instance=respuesta)
            if form.is_valid():
                new_respuesta = form.save()
                return HttpResponseRedirect("/encuestas/%s" % (encuesta_id))
        else:
            form = RespuestasForm(instance=respuesta)
                        
            c = Context({
                'form': form,
            })
            c.update(csrf(request))
            
            return render_to_response("encuestas/edit_respuestas.html", c)    

    except ObjectDoesNotExist:
        raise Http404


def encuesta_crear(request):
    if request.method == 'POST':
        form = EncuestasForm(request.POST)
        if form.is_valid():
            new_encuesta = form.save(commit=False)
            new_encuesta.usuario = request.user
            new_encuesta.save();
            return HttpResponseRedirect("/encuestas/")
    else:
        form = EncuestasForm()

    c = Context({
        'form': form,
    })
    c.update(csrf(request))
    
    return render_to_response("encuestas/edit.html", c)    

def encuesta_editar(request, encuesta_id):
    e = Encuestas.objects.get(pk=encuesta_id)
    if request.method == 'POST':
        form = EncuestasForm(request.POST, instance=e)
        if form.is_valid():
            new_encuesta = form.save()
            return HttpResponseRedirect("/encuestas/")
    else:
         form = EncuestasForm(instance=e)

    c = Context({
        'form': form,
    })
    c.update(csrf(request))
    
    return render_to_response("encuestas/edit.html", c)    
