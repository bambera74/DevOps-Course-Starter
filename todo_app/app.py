from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items, add_item, complete_item, move_to_todo

app = Flask(__name__)
app.config.from_object(Config())



@app.route('/')
def index():
    todolist = get_items()
    todolist_json = todolist.json()

    cards = []
    
    for trello_list in todolist_json:
        for card in trello_list['cards']:
            cards.append({'id': card['id'], 'status': card['idList'], 'title': card['name']})
    return render_template ('index.html', list1=cards)

@app.route('/additem', methods=['POST'])
def additem():
    if request.method =='POST':
        card_name = request.form.get('item_to_add')
        list_id = '64ff08619ed13406181ec929'

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