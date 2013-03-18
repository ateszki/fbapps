# Create your views here.
from django.template import Context, loader
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/encuestas/")
    else:
        form = UserCreationForm()

    c = Context({
        'form': form,
    })
    c.update(csrf(request))
    
    return render_to_response("registration/register.html", c)