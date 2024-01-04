from operator import length_hint
from todo_app.view_model import ViewModel
from todo_app.data.trello_items import Item
import pytest

@pytest.fixture
def test_cards():

    cards = [
            Item('1', 'testcard1', 'todo'),
            Item('2', 'testcard2', 'todo'),
            Item('3', 'testcard3', 'doing'),
            Item('4', 'testcard4', 'doing'),
            Item('5', 'testcard5', 'doing'),
            Item('6', 'testcard6', 'done'),
    ]
    return cards

def test_view_model_handles_items_correctly(test_cards):
    #arrange
    items_in_view_model = ViewModel(test_cards)

    #act
    items = items_in_view_model.items

    #assert
    assert len(items) == 6

def test_view_model_handles_done_items_correctly(test_cards):
    #arrange
    items_in_view_model = ViewModel(test_cards)

    #act
    done_items = items_in_view_model.done_items

    #assert
    assert len(done_items) == 1
    #assert done_items[0].status == "done"

def test_view_model_handles_todo_items_correctly(test_cards):
    #arrange
    items_in_view_model = ViewModel(test_cards)

    #act
    todo_items = items_in_view_model.todo_items

    #assert
    assert len(todo_items) == 2
    #assert todo_items[0].status == "todo"

def test_view_model_handles_doing_items_correctly(test_cards):
    #arrange
    items_in_view_model = ViewModel(test_cards)

    #act
    doing_items = items_in_view_model.done_items

    #assert
    assert len(doing_items) == 3
    #assert doing_items[0].status == "doing"