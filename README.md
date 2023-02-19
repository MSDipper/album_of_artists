<h2 alingn='center'>Альбом</h2>

### Описание проекта:
    Альбом

## Разработка


##### 1) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 2) Выполнить билд docker-compose:
    docker-compose build

##### 3) Применить миграции:
    docker-compose run --rm a_w sh -c "python manage.py migrate"

##### 4) Создать супер юзера:
    docker-compose run --rm a_w sh -c "python manage.py createsuperuser"

##### 5) Запустить docker-compose:
    docker-compose up


