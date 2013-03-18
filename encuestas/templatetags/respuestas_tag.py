from django import template

register = template.Library()

def show_respuestas(pregunta):
    resp = pregunta.respuestas_set.all()
    return {'respuestas': resp, 'pregunta': pregunta, 'encuesta': pregunta.encuesta}

register.inclusion_tag('encuestas/respuestas.html')(show_respuestas)

