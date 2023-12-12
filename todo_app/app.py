import os
from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items, add_item, complete_item, move_to_todo, Item

app = Flask(__name__)
app.config.from_object(Config())



@app.route('/')
def index():
    cards = get_items()

    return render_template ('index.html', list1=cards)

@app.route('/additem', methods=['POST'])
def additem():
    if request.method =='POST':
        card_name = request.form.get('item_to_add')
        list_id = os.getenv('TLIST_BACKLOG')

        add_item(list_id, card_name)
        return redirect (('/'))
    
@app.route('/items/<id>/complete')
def complete_task(id):
    complete_item(id)
    return redirect (('/'))

@app.route('/items/<id>/backtodo')
def back_todo(id):
    move_to_todo(id)
    return redirect (('/'))