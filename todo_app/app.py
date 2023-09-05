from flask import Flask, render_template

from todo_app.flask_config import Config

from todo_app.data.session_items import get_items

from todo_app.data.session_items import add_item

from flask import request, redirect, session

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    todolist = get_items()
    titles = [d['title'] for d in todolist]
    return render_template ('index.html', list1=titles)

@app.route('/additem', methods=['GET', 'POST'])
def additem():
    if request.method =='POST':
        title = request.form.get('title1')
        add_item(title)
        return redirect (('/'))
    
