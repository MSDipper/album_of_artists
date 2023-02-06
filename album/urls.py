from django.urls import path
from album.views import (
                        AlbumView,
                        ExecutorView, 
                        SongView,
                        AddAlbumView,
                        AddExecutorView,
                        AddSongView
                        )


urlpatterns = [
    path('album/', AlbumView.as_view()),
    path('executor/', ExecutorView.as_view()),
    path('song/', SongView.as_view()),
    path('add_album/', AddAlbumView.as_view()),
    path('add_executor/', AddExecutorView.as_view()),
    path('add_song/', AddSongView.as_view()),
]
