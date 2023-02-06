from django.contrib import admin
from album.models import Executor, Album, Song


@admin.register(Executor)
class ExecutorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Album)
class ExecutorAdmin(admin.ModelAdmin):
    list_display = ('executor', 'year_of_issue')
 
  
@admin.register(Song)
class ExecutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_in_album')
