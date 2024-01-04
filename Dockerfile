FROM python:3.9.18-slim-bullseye
WORKDIR /opt/todoapp
ENV FLASK_APP todo_app/app.py
RUN curl -sSL https://install.python-poetry.org | python3
RUN pip install flask
RUN pip install poetry
COPY ./todo_app/*.py todo_app/
COPY ./todo_app/templates/*.html todo_app/templates/
COPY ./todo_app/data/*.py todo_app/data/
COPY ./*.toml /opt/todoapp/
RUN poetry install -n
EXPOSE 5000
ENTRYPOINT flask run
