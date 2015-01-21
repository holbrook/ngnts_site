from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader


from rest_framework import viewsets

from .models import *
from .serializers import *



class BizServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BizService.objects.all()
    serializer_class = BizServiceSerializer


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'l':range(1,5),
    })
    return HttpResponse(template.render(context))
