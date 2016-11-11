# _*_ coding:utf-8 _*_
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from restful.models import Snippet
from restful.serializers import SnippetSerializer

# Create your views here.




@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    展示所以snippets,或创建新的snippet
    """
    if request.method ==  "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def snippet_detail(request, pk):
    """
    修改或删除一个snippet
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method ==  "GET":
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
