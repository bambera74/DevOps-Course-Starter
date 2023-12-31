import os, requests, json

class Item:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_trello_card(cls, card):
        return cls(card['id'], card['name'], card['listName'])

def get_items():
    """
    Fetches all saved items from the Trello API.

    Returns:
        list: The list of saved items.
    """
    
    url = f'https://api.trello.com/1/boards/{os.getenv("TRELLO_BOARDID")}/lists'

    query ={
        'cards' : 'open',
        'card_fields' : 'name,listName',
        'key' : os.getenv('TRELLO_APIKEY'),
        'token' : os.getenv('TRELLO_TOKEN'),
    }

    todolist = requests.request("GET", url, params=query)
    todolist_json = todolist.json()

    cards = []
  
    for trello_list in todolist_json:
        for card in trello_list['cards']:
            card['listName'] = trello_list['name']
            cards.append(Item.from_trello_card(card))
    return cards

def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(list_id, card_name):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """

    url = "https://api.trello.com/1/cards"

    headers = {
        "Accept": "application/json"
                }

    query = {
        'idList': os.getenv('TLIST_BACKLOG'),
        'key': os.getenv('TRELLO_APIKEY'),
        'token': os.getenv('TRELLO_TOKEN'),
        'name' : card_name
    }

    response = requests.request("POST", url, headers=headers, params=query)
    return response

    #print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    #items = get_items()

    # Determine the ID for the item based on that of the previously added item
    #id = items[-1]['id'] + 1 if items else 0

    #item = { 'id': id, 'title': title, 'status': 'Not Started' }

    # Add the item to the list
    #items.append(item)
    #session['items'] = items

    #return item


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item

def complete_item(id):

    url = "https://api.trello.com/1/cards/" + id 

    headers = {
    "Accept": "application/json"
    }

    query = {
    'key': os.getenv('TRELLO_APIKEY'),
    'token': os.getenv('TRELLO_TOKEN'),
    'idList': os.getenv('TLIST_DONE')
    }

    response = requests.request("PUT", url, headers=headers, params=query)
    return response

def move_to_todo(id):

    url = "https://api.trello.com/1/cards/" + id 

    headers = {
    "Accept": "application/json"
    }

    query = {
    'key': os.getenv('TRELLO_APIKEY'),
    'token': os.getenv('TRELLO_TOKEN'),
    'idList': os.getenv('TLIST_TODO')
    }

    response = requests.request("PUT", url, headers=headers, params=query)
    return response