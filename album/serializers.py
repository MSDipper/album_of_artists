from rest_framework import serializers
from album.models import Album, Executor, Song


class AlbumSerializer(serializers.ModelSerializer):
    """ Добавление отзыва """
    class Meta:
        model = Album
        fields = '__all__'


class ExecutorSerializer(serializers.ModelSerializer):
    """ Добавление отзыва """
    class Meta:
        model = Executor
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    """ Добавление отзыва """
    class Meta:
        model = Song
        fields = '__all__'