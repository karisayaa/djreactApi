from rest_framework import viewsets
from .selializers import PostSerializer
from corepost.models import Post


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()