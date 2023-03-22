![yamdb_workflow](https://github.com/GlebMudrov/foodgram-project-react/actions/workflows/foodgram_main.yml/badge.svg)
# Проект Foodgram

### http://foodgram-mudrov.hopto.org/
### 84.201.164.97

### Админ-зона:
user: admin
password: admin

### Описание проекта:
Foodgram - онлайн-сервис, где пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Технологии :
- Python
- Django 
- Django REST Framework
- Docker
- Gunicorn
- Nginx
- PostgreSQL

### Запуск проекта локально (адаптировано под Windows):
Клонировать репозиторий и перейти в него в командной строке (использовать ssh):
```
git@github.com:GlebMudrov/foodgram-project-react.git
```
```
cd foodgram-project-react/infra/
```
Создать файл .env и заполнить его данными:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
Запуск проекта в контейнерах Docker:
```
docker-compose up -d
```
Провести миграции, создать суперпользователя, собрать статику и импорт тегов в базу данных:
```
docker-compose exec backend python manage.py makemigrations users
docker-compose exec backend python manage.py makemigrations recipes
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py collectstatic --no-input
docker-compose exec backend python manage.py import_data
```
Проект станет доступен по адресу http://localhost/
Админ-зона: http://localhost/admin

### Автор проекта:  <a href= "https://github.com/GlebMudrov">__Мудров Глеб__<a/>