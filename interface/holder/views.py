from django.http import HttpResponse
from sympy import * 
# from fenics import *
# from mshr import *
import numpy as np
import datetime
import os
import sys
# sys.path.append("containers/automations")
# from .myPackages.autopush import autoPush

def index(request):
    x = Symbol('x')
    f = 5*x**3 + 12
    d = f.diff(x)
    html = f"<html><body>The Derivate of  5*x**3+12 := {d}</body></html>" 
    return HttpResponse(html)

def partial(request):
    x = Symbol('x')
    y = Symbol('y')
    fa = 6*x*y + x**2*y + 26
    html = f"<html><body>The Partial Derivate of 6*x*y + x**2*y + 26 is := {diff(fa,x)} </body></html>" 
    return HttpResponse(html)

def processOne(request):
    # < add the process code here >
    html = "<html><body>Under Construction , hang on! </body></html>" 
    return HttpResponse(html)

def currentTime(request):
    html = f"Current time : {datetime.datetime.now()}"
    return HttpResponse(html)

def clickPush(request):

    """ from ~/containers/automations/autopush import autopush
    os.chdir("containers/automations/")
    from autopush import autoPush """
    html = f"<form method=\"post\"> Button exists here :- <button type=\"submit\" name=\"activate\">Activate</button> </form>"
    """ if request.method == 'POST' and 'activate' in request.POST:
        autoPush()
        print("inner") """ # unleash these comments to engage in git push

    return HttpResponse(html)

def lychrel(request):
    html = f"Current time : {datetime.datetime.now()}"
    return HttpResponse(html)