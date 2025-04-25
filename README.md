# ⚍ Libroll - server

Серверная часть приложения для учёта созданных займов книг в библиотеке. Написано на Django с использованием PostgreSQL и REST Framework. База данных может быть удалённой или локальной. Для удалённой используется сервис Neon. Для локальной база SQLite. Приложение может работать как локально так и на хостинге Vercel. 

### Конечные точки API

- Общие
  - `GET`       `/` - Приветствие от сервера.
  - `GET`       `/health` - Проверка живоспособности сервера.
  - `GET`       `/database-health` - Проверка живоспособности базы данных.
  - `GET`       `/stats` - Получение статистики по записям: количество книг, пользователей, займов всего, активных и неактивных.
- Аутентификация
  - `POST`      `/auth/login` - Вход пользователя.
  - `POST`      `/auth/register` - Регистрация нового суперпользователя.
- Книги
  - `GET`       `/books` - Получить список всех книг.
  - `POST`      `/books` - Добавить новую книгу.
  - `GET`       `/books/:id` - Получить информацию о книге.
  - `PUT`       `/books/:id` - Обновить информацию о книге.
  - `DELETE`    `/books/:id` - Удалить книгу.
- Пользователи
  - `GET`       `/users` - Получить список всех пользователей.
  - `POST`      `/users` - Добавить нового пользователя.
  - `GET`       `/users/:id` - Получить информацию о пользователе.
  - `PUT`       `/users/:id` - Обновить информацию о пользователе.
  - `DELETE`    `/users/:id` - Удалить пользователя.
- Займы
  - `GET`       `/borrows` - Получить список всех займов.
  - `POST`      `/borrows` - Создать новый заём.
  - `GET`       `/borrows/:id` - Получить информацию о займе.
  - `PUT`       `/borrows/:id` - Обновить информацию о займе.
  - `DELETE`    `/borrows/:id` - Удалить заём.


### Установка и запуск

Для установки зависимостей выполните команду:

```sh
pip install -r requirements.txt
```

Чтобы запустить приложение локально, убедитесь, что у вас установлены Node JS, PostgreSQL, и существует `.env` файл в корне проекта. Пример `.env` файла приведён ниже. 

```ini
# Django
DJANGO_SECRET_KEY=django-insecure-key
DEBUG=true

# Database
LOCAL=true

PGDATABASE=ndb_database
PGUSER=user
PGPASSWORD=password
PGHOST=host.aws.neon.tech
PGPORT=5432

# JWT
SECRET_KEY=:(
```

Для запуска сервера выполните команду:

```sh
python manage.py runserver
```

<!-- TODO:
 - [x] This was made very poor and with DeepSeek. Cuz Copilot now works wery bad, alaways gives errors... :(
 - [x] Make it alive from Vercel
 -->
