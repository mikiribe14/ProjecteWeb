# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from HTTP import HTTPRequest

# Create your views here.
def mainpage(request):
    return HTTPRequest("<html><body>Holaaaa<body></html>")
