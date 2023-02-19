<h2 alingn='center'>Альбом</h2>

### Описание проекта:
    Альбом

## Разработка



##### 1) Выполнить билд docker-compose:
    docker-compose build

##### 2) Применить миграции:
    docker-compose run --rm a_w sh -c "python manage.py migrate"

##### 3) Создать супер юзера:
    docker-compose run --rm a_w sh -c "python manage.py createsuperuser"

##### 4) Запустить docker-compose:
    docker-compose up


