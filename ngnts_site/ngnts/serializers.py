from rest_framework import routers, serializers, viewsets
from rest_framework.views import *
from .models import *
from django.contrib.auth.models import *


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users)
        return Response(serializer.data)

class BizServiceSerializer(serializers.ModelSerializer):
    #posts = serializers.HyperlinkedIdentityField('posts', view_name='userpost-list', lookup_field='username')

    class Meta:
        model = BizService
        fields = ('name', )


