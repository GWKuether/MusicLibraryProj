from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer
from .models import Song

@api_view(['GET', 'POST'])
def songs_list(request):

    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def song_detail(request, pk):
    try:
        song=Song.objects.get(pk=pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


