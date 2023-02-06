from django.db import models


class Executor(models.Model):
    """ Исполнитель """
    name = models.CharField(max_length=150, verbose_name='Название')
    
    
    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'
    
    def __str__(self):
        return self.name


class Album(models.Model):
    """ Альбом """
    executor = models.ForeignKey(
        Executor, 
        verbose_name='Исполнитель',
        on_delete=models.SET_NULL,
        null=True, 
        blank=True
        )
    year_of_issue = models.DateField(auto_now_add=False, verbose_name='Год выпуска')
    
    
    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбом'
    
    def __str__(self):
        return f'{self.executor}'
    

class Song(models.Model):
    """ Песня """
    name = models.CharField(max_length=150, verbose_name='Название')
    number_in_album = models.PositiveSmallIntegerField(
        unique=True, 
        verbose_name='Порядковый номер в альбоме', 
        default=''
        )
    
    
    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'
    
    def __str__(self):
        return self.name