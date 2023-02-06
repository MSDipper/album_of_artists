from rest_framework import generics
from rest_framework.views import APIView
from album.models import Album, Executor, Song
from album.serializers import AlbumSerializer, ExecutorSerializer, SongSerializer
from rest_framework.response import Response


class AlbumView(generics.ListAPIView):
    ''' Вывод записей альбома '''
    queryset = album = Album.objects.all()
    serializer_class = AlbumSerializer


class AddAlbumView(generics.CreateAPIView):
    ''' Добавление записей альбома '''
    serializer_class = AlbumSerializer


class ExecutorView(generics.ListAPIView):
    ''' Вывод исполнителей '''
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer


class AddExecutorView(generics.CreateAPIView):
    ''' Добавление исполнителей '''
    serializer_class = ExecutorSerializer


class SongView(generics.ListAPIView):
    ''' Вывод песни '''
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AddSongView(generics.CreateAPIView):
    ''' Добавление песни '''
    serializer_class = SongSerializer