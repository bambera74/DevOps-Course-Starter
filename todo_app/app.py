from flask import Flask, render_template

from todo_app.flask_config import Config

from todo_app.data.trello_items import get_items

from todo_app.data.trello_items import add_item

from flask import request, redirect, session

app = Flask(__name__)
app.config.from_object(Config())



@app.route('/')
def index():
    todolist = get_items()
    tasks = [d['name'] for d in todolist]
    return render_template ('index.html', list1=tasks)

@app.route('/additem', methods=['POST'])
def additem():
    if request.method =='POST':
        title = request.form.get('title1')
        add_item(title)
        return redirect (('/'))
    
