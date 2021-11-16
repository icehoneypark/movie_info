from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CommunitySerializer
from .models import Community


@api_view(['GET', 'POST'])
def community_create(request):
    if request.method == 'GET':
        communities = request.user.community_set.all()
        serializer = CommunitySerializer(communities, many=True)
        return Response(serializer.data)
    else:
        print(request.user)
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def community_delete(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    if request.method == 'PUT':
        serializer = CommunitySerializer(community, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        community.delete()
        return Response({ 'id': community_pk })