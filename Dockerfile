FROM python:3.9.18-slim-bullseye as base
WORKDIR /opt/todoapp
RUN pip install flask
RUN pip install poetry
COPY ./todo_app/*.py todo_app/
COPY ./todo_app/templates/*.html todo_app/templates/
COPY ./todo_app/data/*.py todo_app/data/
COPY ./*.toml /opt/todoapp/
RUN poetry install -n

FROM base as development
ENV FLASK_APP todo_app/app.py
EXPOSE 5000
ENTRYPOINT flask run --host=0.0.0.0

FROM base as production
EXPOSE 8000
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"
