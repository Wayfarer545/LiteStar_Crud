FROM python:3.12.9-slim

ENV POETRY_VERSION=1.8.3

RUN pip install --upgrade pip && \
    pip install "poetry==$POETRY_VERSION"

WORKDIR /app
COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-root
COPY ./src .
RUN poetry run alembic upgrade head

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
