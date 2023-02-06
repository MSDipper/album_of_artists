<h2 alingn='center'>Альбом</h2>

### Описание проекта:
    Альбом

## Разработка



##### 1) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 2) Создать виртуальное окружение

    python -m venv venv
    
##### 3) Активировать виртуальное окружение

    venv\Scripts\activate.bat - Windows

    venv/bin/activate - Linux

##### 4) Выполнить билд docker-compose:
    docker-compose build

##### 5) Применить миграции:
    docker-compose run --rm a_w sh -c "python manage.py migrate"

##### 6) Создать супер юзера:
    docker-compose run --rm a_w sh -c "python manage.py createsuperuser"

##### 7) Запустить docker-compose:
    docker-compose up


