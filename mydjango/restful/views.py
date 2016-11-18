# _*_ coding:utf-8 _*_
from restful.models import Snippet
from restful.serializers import SnippetSerializer
from restful.serializers import UserSerializer
from django.contrib.auth.models import User
from restful.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import detail_route

# Create your views here.

class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)
    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retri
    eve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer
                                    ])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` acti
    ons.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


