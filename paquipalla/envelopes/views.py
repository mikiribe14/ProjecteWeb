# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def mainpage(request):
    return HttpResponse('<html><body><title>"Curriculum vitae"</title><h1>Curriculum vitae</h1><p>Aquest es un paragraf de prova per veure com funciona el <strong>strong</strong> i la <em>cursiva</em>.</p><h3 title="Formacio">Formacio academica</h3><ul><li>Primaria</li><li>ESO</li><li>Batx</li><li>Uni</li></ul><h3 title="Experiencia">Experiencia laboral</h3><ol type="i"><li><strong>2010-2012</strong>: Collir</li><li><strong>2012-2014</strong>: Cope<ul><li>Embalador</li><li>Maquines</li><li>Traspaleta</li></ul></li><li><strong>2014-2017</strong>: Flix</li></ol><p>Links dinteres:</p><ul><li><a>href="https://www.google.com/"</a>Google</li><li><a title="Enlace a Facebook" href="https://www.facebook.com/"</a>Facebook</li><li><a title="Enlace a Twitter" href="https://twitter.com/?lang=es"</a>Twitter</li><li><a href="http://www.eps.udl.cat/ca/"</a>EPS</li><li><a title="Mister"href="https://mister.mundodeportivo.com/"</a>Misteeer</li></ul></body></html>'
)
