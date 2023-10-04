from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items, add_item

app = Flask(__name__)
app.config.from_object(Config())



@app.route('/')
def index():
    todolist = get_items()
    todolist_json = todolist.json()
    #json_formatted_str = json.dumps (todolist_json, ",")

    #cards = []
    items = []
    for card in todolist_json:
        #card['status'] - todolist_json['name']
        item = card['id'], card['name'], card['status']
        items.append(item)
        #cards.append(card)
    
    #tasks = [d['name'] for d in todolist]
    return render_template ('index.html', list1=items)

@app.route('/additem', methods=['POST'])
def additem():
    if request.method =='POST':
        card_name = request.form.get('title1')
        list_id = '64ff08619ed13406181ec929'

        add_item(list_id, card_name)
        return redirect (('/'))
    
