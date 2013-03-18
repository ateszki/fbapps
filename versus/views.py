from django.forms.models import modelformset_factory
from django.template import Context, loader, RequestContext
from versus.models import Versus,VersusForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
@login_required

def index(request):
    #return HttpResponse("Bienvenido!")
    if Versus.objects.count() > 0 :
        v = Versus.objects.all()
        c = Context({
            'versus': v,
        })
    else:
        c = Context({
            'versus': '',
        })
    t = loader.get_template('versus/index.html')
    return HttpResponse(t.render(c))

def editar(request, versus_id = None):
    try:
        if versus_id is None:
            versus = Versus()
            versus.usuario = request.user
        else:
            versus = Versus.objects.get(pk=versus_id)
            
        if request.method == 'POST':
            form = VersusForm(request.POST, request.FILES, instance=versus)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/versus/")
        else:
            form = VersusForm(instance=versus)
    
        c = Context({
            'form': form,
        })
        c.update(csrf(request))
        
        return render_to_response("versus/edit.html", c)    
    except ObjectDoesNotExist:
        raise Http404
    
def delete(request, versus_id):
    try:
        versus = Versus.objects.get(pk=versus_id)
        versus.delete()
        return HttpResponseRedirect("/versus/")
    except ObjectDoesNotExist:
        raise Http404
    