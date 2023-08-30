from flask import Flask, render_template

from todo_app.flask_config import Config

from todo_app.data.session_items import get_items

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    todolist = get_items()
    titles = [d['title'] for d in todolist]
    return render_template ('index.html', titles = titles)

