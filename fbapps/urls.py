from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fbapps.views.home', name='home'),
    # url(r'^fbapps/', include('fbapps.foo.urls')),

    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),
    (r'^accounts/register/$', 'registration.views.register'),

    #encuestas
    url(r'^encuestas/$','encuestas.views.index'),
    url(r'^encuestas/(?P<encuesta_id>\d+)/$','encuestas.views.detail'),
    url(r'^encuestas/add$','encuestas.views.encuesta_crear'),
    url(r'^encuestas/edit/(?P<encuesta_id>\d+)/$','encuestas.views.encuesta_editar'),
    url(r'^encuestas/(?P<encuesta_id>\d+)/add/$','encuestas.views.pregunta'),
    url(r'^encuestas/(?P<encuesta_id>\d+)/(?P<pregunta_id>\d+)/$','encuestas.views.pregunta'),
    url(r'^encuestas/(?P<encuesta_id>\d+)/(?P<pregunta_id>\d+)/delete/$','encuestas.views.pregunta_delete'),
    url(r'^encuestas/(?P<encuesta_id>\d+)/(?P<pregunta_id>\d+)/mover/(?P<sentido>\w+)/$','encuestas.views.pregunta_mover'),
    url(r'^encuestas/(?P<encuesta_id>\d+)/(?P<pregunta_id>\d+)/add/$','encuestas.views.respuesta'),
    url(r'^encuestas/(?P<encuesta_id>\d+)/(?P<pregunta_id>\d+)(:?/(?P<respuesta_id>\d+))?/$','encuestas.views.respuesta'),
    url(r'^encuestas/(?P<encuesta_id>\d+)/(?P<pregunta_id>\d+)/(?P<respuesta_id>\d+)/delete/$','encuestas.views.respuesta_delete'),
    url(r'^encuestas/(?P<encuesta_id>\d+)/(?P<pregunta_id>\d+)/(?P<respuesta_id>\d+)/mover/(?P<sentido>\w+)/$','encuestas.views.respuesta_mover'),
    url(r'^encuestas/(?P<encuesta_id>\d+)/(?P<pregunta_id>\d+)/(?P<accion>\w+)/$','encuestas.views.pregunta'),
    
    #versus
    url(r'^versus/$','versus.views.index'),
    url(r'^versus/edit(:?/(?P<versus_id>\d+))?/$','versus.views.editar'),
    url(r'^versus/delete/(?P<versus_id>\d+)/$','versus.views.delete'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # media files
    url (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
