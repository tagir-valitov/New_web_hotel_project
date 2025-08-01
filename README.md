# New Web Hotel Project

Веб-приложение для управления отелями, построенное на FastAPI с использованием PostgreSQL и SQLAlchemy.

## Описание

Это веб-приложение предоставляет API для управления:
- Отелями
- Номерами
- Пользователями
- Бронированиями

## Технологии

- **FastAPI** - современный веб-фреймворк для Python
- **SQLAlchemy** - ORM для работы с базой данных
- **PostgreSQL** - реляционная база данных
- **Alembic** - миграции базы данных
- **Pydantic** - валидация данных
- **Uvicorn** - ASGI сервер

## Установка и запуск

### Предварительные требования

- Python 3.11+
- PostgreSQL

### Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/tagir-valitov/New_web_hotel_project.git
cd New_web_hotel_project
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
```

3. Активируйте виртуальное окружение:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Установите зависимости:
```bash
pip install -r requirements.txt
```

5. Создайте файл `.env` с настройками базы данных:
```env
DB_HOSTS=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASS=your_password
DB_NAME=hotel_db
```

6. Запустите миграции:
```bash
alembic upgrade head
```

7. Запустите приложение:
```bash
uvicorn app.main:app --reload
```

Приложение будет доступно по адресу: http://127.0.0.1:8000

## API Документация

После запуска приложения, документация API будет доступна по адресу:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Структура проекта

```
app/
├── __init__.py
├── main.py          # Точка входа приложения
├── config.py        # Конфигурация
├── database.py      # Настройки базы данных
├── bookings/        # Модуль бронирований
├── hotels/          # Модуль отелей
├── rooms/           # Модуль номеров
└── users/           # Модуль пользователей
```

## Лицензия

MIT License
