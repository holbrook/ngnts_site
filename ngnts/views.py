from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader

from models import *


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    template = loader.get_template('ngnts/index.html')
    context = RequestContext(request, {
        'l':range(1,5),
    })
    return HttpResponse(template.render(context))
