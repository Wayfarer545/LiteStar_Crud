# Basic CRUD on LiteStar. 
Простейший DDD/CA CRUD сервис на фреймворке LiteStar.
Сервис полностью работоспособен. 
___
Stack:
- python 3.12.9
- LiteStar 2.15.2
- litestar-granian
- litestar-asyncpg (не имплементирован)
- Poetry 1.8.3
- Alembic 1.15.2
- SQLAlchemy/Advanced-alchemy
- Postgres 17
- Docker/docker compose
___
### Запуск 
На машине должен быть глобально установлен poetry.

1. Клонировать репозиторий и перейти в корень проекта:
    ```bash
   git clone https://github.com/Wayfarer545/LiteStar_Crud.git && cd LiteStar_Crud
    ```
2. Установить зависимости:
    ```bash
    poetry install --no-root
    ```
3. Создать в корне проекта файл с переменными окружения .env по образу example.env:
4. Применить миграции:
   ```bash
   poetry run alembic upgrade head
   ```
5. Запустить сервис с помощью granian:
   ```bash
   poetry run litestar --app src.app:app run
   ```
### Запуск в docker контейнере
На машине должен быть установлен и запущен docker и установлен  
docker compose v2 плагин.
1. Клонировать репозиторий и перейти в корень проекта:
    ```bash
   git clone https://github.com/Wayfarer545/LiteStar_Crud.git && cd LiteStar_Crud
    ```
2. выполнить:
   ```bash
   sudo docker compose -f ./docker/compose.yml up -d --build
   ```
Конфигурация compose поднимает базу данных postgres 18 со стандартными кредсами
postgres/postgres и рабочей базой данных litestar.
Переменные окружения для простоты занесены в compose.yml, поэтому дополнительно  
ничего прописывать не нужно. 

Автоматическая документация будет доступна по стандартным адресам лайтстар.