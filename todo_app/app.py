from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items, add_item
from todo_app.views import ViewModel

app = Flask(__name__)
app.config.from_object(Config())



@app.route('/')
def index():
    todolist = get_items()
    todolist_json = todolist.json()

    cards = []
    
    for trello_list in todolist_json:
        for card in trello_list['cards']:
            cards.append(card)
 
    return render_template ('index.html', list1=cards)


@app.route('/additem', methods=['POST'])
def additem():
    if request.method =='POST':
        card_name = request.form.get('title1')
        list_id = '64ff08619ed13406181ec929'

        add_item(list_id, card_name)
        return redirect (('/'))
    
