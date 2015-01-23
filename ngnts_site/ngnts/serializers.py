from rest_framework import routers, serializers, viewsets
from rest_framework.views import *
from .models import *


class BizCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BizCategory
        fields = ('name', )

class BizServiceSerializer(serializers.ModelSerializer):
    #posts = serializers.HyperlinkedIdentityField('posts', view_name='userpost-list', lookup_field='username')

    class Meta:
        model = BizService
        fields = ('name', 'category','level',)


