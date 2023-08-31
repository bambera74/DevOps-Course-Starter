from flask import Flask, render_template

from todo_app.flask_config import Config

from todo_app.data.session_items import get_items

from todo_app.data.session_items import add_item

from flask import request

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    todolist = get_items()
    titles = [d['title'] for d in todolist]
    title_one = titles[0]
    title_two = titles[1]
    title_three = titles[2]
    return render_template ('index.html', title_one = title_one, title_two = title_two, title_three = title_three)
# Can turn into a for loop if I have time

@app.route('/additem', methods=['GET', 'POST'])
def additem():
    title = request.form.get('title')
    add_item(title)
    return index()
