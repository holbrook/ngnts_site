from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader


from rest_framework import viewsets
from rest_framework.views import APIView

from .models import *
from .serializers import *

def index_view(request):
    template = loader.get_template('index.html')

    services = {}

    types = BizCategory.objects.all()
    levels = BizLevel.objects.all()
    services = BizService.objects.all()


    context = RequestContext(request, {
        'types':types,
        'levels': levels,
        'services': services,
    })
    return HttpResponse(template.render(context))


class BizServiceViewSet(viewsets.ModelViewSet):
    # """
    # API endpoint that allows users to be viewed or edited.
    # """
    queryset = BizService.objects.all()
    serializer_class = BizServiceSerializer

    def list(self, request):
        queryset = BizService.objects.all()
        serializer = BizServiceSerializer(queryset, many=True)
        biz_types = BizCategory.objects.all()
        biz_services = BizService.objects.all()

        return Response({
            # 'types':biz_types,
            'services':serializer.data})


    def retrieve(self, request, pk=None):
        queryset = BizService.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = BizServiceSerializer(user)
        return Response(serializer.data)


