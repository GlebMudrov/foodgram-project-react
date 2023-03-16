# Foodgram (в процессе разработки)

### Описание проекта:
Foodgram - онлайн-сервис, где пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Технологии :
- Python
- Django
- Django REST Framework

### Запуск проекта локально:
Клонировать репозиторий и перейти в него в командной строке (использовать ssh):
```
git@github.com:GlebMudrov/foodgram-project-react.git
```
```
cd foodgram-project-react
```
Создание и запуск виртуального окружения:
```
python -m venv venv
. venv/scripts/activate
api
```
Выполнить миграции, создать суперпользователя, импортировать ингриденты в базу данных, собрать статику::
```
cd backend/
python manage.py migrate --run-syncdb
python manage.py createsuperuser
python manage.py load_data
python manage.py collectstatic --no-input
```