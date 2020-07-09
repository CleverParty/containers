from django.http import HttpResponse
from sympy import * 

def index(request):
    x = Symbol('x')
    f = 5*x**3+12
    d = f.diff(x)
    html = "<html><body>The Differtial of 5x^3 + 12 is : %s.</body></html>" % d
    return HttpResponse(html)