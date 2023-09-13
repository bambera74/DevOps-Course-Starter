import os, requests

api_key = os.getenv('TRELLO_APIKEY')
api_token = os.getenv('TRELLO_TOKEN')

def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    
    url = 'https://api.trello.com/1/boards/64ff08619ed13406181ec926/cards'

    query ={
        'fields' : 'name',
        'key' : api_key,
        'token' : api_token
    }

    todolist = requests.request("GET", url, params=query)
    return todolist.json()
    #tasks = [d['name'] for d in cards]
    #return render_template ('index.html', list1=tasks)

    #return session.get('items', _DEFAULT_ITEMS.copy())

#print ('items', _DEFAULT_ITEMS.copy())

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


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    items = get_items()

    # Determine the ID for the item based on that of the previously added item
    id = items[-1]['id'] + 1 if items else 0

    item = { 'id': id, 'title': title, 'status': 'Not Started' }

    # Add the item to the list
    items.append(item)
    session['items'] = items

    return item


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
