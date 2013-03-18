from django.forms import ModelForm, forms
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Encuestas(models.Model):
    def __unicode__(self):
        return self.nombre
    
    nombre = models.CharField(max_length=500)
    publicacion = models.DateTimeField('fecha publicacion')
    usuario = models.ForeignKey(User)

    def mover(self,pregunta, sentido):
        #toma la lista de ordenes
        o = self.get_preguntas_order()
        
        if sentido not in ['ABAJO','ARRIBA']: 
            otro = self.preguntas_set.get(pk=sentido)
            o.insert(o.index(otro.id), o.pop(o.index(pregunta.id)))
        else:        
            if sentido == 'ABAJO':
                otro = pregunta.get_next_in_order()
            elif sentido == 'ARRIBA':
                otro = pregunta.get_previous_in_order()

            #toma las posiciones en la lista
            a, b = o.index(pregunta.id), o.index(otro.id)
            #invierte las posiciones
            o[b], o[a] = o[a], o[b]
        
        self.set_preguntas_order(o)
        
class EncuestasForm(ModelForm):
    class Meta:
        model = Encuestas


class Preguntas(models.Model):
    def __unicode__(self):
        return self.pregunta
    
    encuesta = models.ForeignKey(Encuestas)
    pregunta = models.CharField(max_length=500)

    def mover(self,respuesta, sentido):
        #toma la lista de ordenes
        o = self.get_respuestas_order()
        
        if sentido not in ['ABAJO','ARRIBA']: 
            otro = self.respuestas_set.get(pk=sentido)
            o.insert(o.index(otro.id), o.pop(o.index(respuesta.id)))
        else:        
            if sentido == 'ABAJO':
                otro = respuesta.get_next_in_order()
            elif sentido == 'ARRIBA':
                otro = respuesta.get_previous_in_order()

            #toma las posiciones en la lista
            a, b = o.index(respuesta.id), o.index(otro.id)
            #invierte las posiciones
            o[b], o[a] = o[a], o[b]
        
        self.set_respuestas_order(o)
        
    class Meta:
        order_with_respect_to = 'encuesta'
        
class PreguntasForm(ModelForm):
    class Meta:
        model = Preguntas

class Respuestas(models.Model):
    def __unicode__(self):
        return self.respuesta
    pregunta = models.ForeignKey(Preguntas)
    respuesta = models.CharField(max_length=500)
    class Meta:
        order_with_respect_to = 'pregunta'

class RespuestasForm(ModelForm):
    class Meta:
        model = Respuestas

