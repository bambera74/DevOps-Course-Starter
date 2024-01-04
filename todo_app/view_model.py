#@classmethod
class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items
    
    @property
    def done_items(self):
        done_items = [item for item in self._items if item.status == "done"]         
        return done_items
    
    @property
    def todo_items(self):
        todo_items = [item for item in self._items if item['status']=="todo"]         
        return todo_items
    
    @property
    def doing_items(self):
        doing_items = [item for item in self._items if item['status']=="doing"]         
        return doing_items