FROM python:3.12.9-slim

ENV POETRY_VERSION=1.8.3
ENV PG_HOST=postgres
ENV PG_PORT=5432
ENV PG_USER=postgres
ENV PG_PASSWORD=postgres
ENV PG_DATABASE=litestar

RUN pip install --upgrade pip && \
    pip install "poetry==$POETRY_VERSION"

WORKDIR /app
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root
COPY ./src ./src
COPY ./migrations/ ./migrations
COPY ./alembic.ini ./
COPY ./entrypoint.sh .

EXPOSE 8000

RUN chmod +x ./entrypoint.sh

# Применение миграций и запуск приложения
ENTRYPOINT ["./entrypoint.sh"]
