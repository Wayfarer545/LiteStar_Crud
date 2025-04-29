# Basic CRUD on LiteStar. 
Сделал скелет в канонах DDD и чистой архитектуры, однако пока не разделил слой репрезентации и сервис.  
Необходимо оформить контроллер и юзкейсы подобающим образом, чтобы не было мешанины.
___
Stack:
- python 3.12.9
- LiteStar 2.15.2
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
   git clone git@github.com:Wayfarer545/LiteStar_Crud.git && cd LiteStar_Crud
    ```
2. Установить зависимости:
    ```bash
    poetry install
    ```
3. Создать в корне проекта файл с переменными окружения .env по образу example.env:
4. 
   