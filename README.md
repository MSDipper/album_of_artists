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

##### 4) Устанавливить зависимости:

    pip install -r req.txt

##### 5) Выполнить билд docker-compose:
    docker-compose build

##### 6) Применить миграции:
    docker-compose run --rm a_w sh -c "python manage.py migrate"

##### 7) Создать супер юзера:
    docker-compose run --rm a_w sh -c "python manage.py createsuperuser"

##### 8) Запустить docker-compose:
    docker-compose up


