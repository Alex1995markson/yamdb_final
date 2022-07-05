# yamdb_final
![Build Status](https://github.com/Alex1995markson/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=master&event=push)

# Описание 

Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий может быть расширен.

### Как запустить проект: 
Все описанное ниже относится к ОС Linux. 
Клонируем репозиторий и и переходим в него: 
```bash 
git clone git@github.com:Alex1995markson/yamdb_final.git
cd yamdb_final 
cd api_yamdb 
``` 
 
Создаем и активируем виртуальное окружение: 
```bash 
python3 -m venv venv 
source /venv/bin/activate
python -m pip install --upgrade pip 
``` 
 
Ставим зависимости из requirements.txt: 
```bash 
pip install -r requirements.txt 
``` 

Переходим в папку с файлом docker-compose.yaml: 
```bash 
cd infra 
``` 
 
Поднимаем контейнеры: 
```bash 
docker-compose up -d --build 
``` 

Миграции: 
```bash 
docker-compose exec web python manage.py makemigrations reviews 
``` 
```bash 
docker-compose exec web python manage.py migrate --run-syncdb
``` 

Создаем суперпользователя: 
```bash 
docker-compose exec web python manage.py createsuperuser 
``` 

Србираем статику: 
```bash 
docker-compose exec web python manage.py collectstatic --no-input 
``` 

Создаем дамп базы данных: 
```bash 
docker-compose exec web python manage.py dumpdata > dumpPostrgeSQL.json 
``` 

Останавливаем контейнеры: 
```bash 
docker-compose down -v 
``` 

### Пример наполнения .env (не включен в текущий репозиторий) расположенный по пути infra/.env 
``` 
DB_ENGINE=django.db.backends.postgresql 
DB_NAME=postgres 
POSTGRES_USER=postgres 
POSTGRES_PASSWORD=postgres 
DB_HOST=db 
DB_PORT=5432 
``` 
### API YaMDb 
Документация доступна по: http://51.250.25.216/redoc/ 

## Над проектом работал:

**[Маценко Александр](https://github.com/Alex1995markson)**
