from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required()
def logado(request):
    return HttpResponse("<h3>Usuario Logado</h3>")
