from django.http import HttpResponse
from sympy import * 
# from fenics import *
# from mshr import *
import numpy as np

def processOne(request):
    # < add the process code here >
    html = "<html><body>Under Construction , hang on! </body></html>" 
    return HttpResponse(html)

def index(request):
    x = Symbol('x')
    f = 5*x**3+12
    d = f.diff(x)
    html = "<html><body>The Derivate of  5*x**3+12 := %s </body></html>" % d
    return HttpResponse(html)

def partial(request):
    x = Symbol('x')
    y = Symbol('y')
    fa = 6*x*y + x**2*y + 26
    html = "<html><body>The Partial Derivate of 6*x*y + x**2*y + 26 is := %s </body></html>" % diff(fa,x)
    return HttpResponse(html)


