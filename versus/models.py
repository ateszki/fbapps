from django.forms import ModelForm, forms
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Versus(models.Model):
    def __unicode__(self):
        return self.nombre
    
    nombre = models.CharField(max_length=500)
    texto1 = models.CharField(max_length=500)
    imagen1 = models.ImageField(upload_to='versus')
    texto2 = models.CharField(max_length=500)
    imagen2 = models.ImageField(upload_to='versus')
    publicacion = models.DateTimeField('fecha publicacion')
    usuario = models.ForeignKey(User)

class VersusForm(ModelForm):
    class Meta:
        model = Versus
