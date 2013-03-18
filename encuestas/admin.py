from encuestas.models import Encuestas, Preguntas, Respuestas
from django.contrib import admin

class RespuestasInline(admin.TabularInline):
    model = Respuestas
    extra = 1

class PreguntasAdmin(admin.ModelAdmin):
    list_filter = ['encuesta']
    inlines = [RespuestasInline]

admin.site.register(Encuestas)
admin.site.register(Preguntas, PreguntasAdmin)
