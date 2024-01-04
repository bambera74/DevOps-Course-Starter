from operator import length_hint
from todo_app.view_model import ViewModel
import pytest

@pytest.fixture
def test_cards():

    cards = [
            Item('1', 'todo', 'testcard1'),
            Item('2', 'todo', 'testcard2'),
            Item('3', 'doing', 'testcard3'),
            Item('4', 'doing', 'testcard4'),
            Item('5', 'doing', 'testcard5'),
            Item('6', 'done', 'testcard6'),
    ]
    return cards

def test_view_model_handles_items_correctly(test_cards):
    #arrange
    cards = test_cards

    #act
    items_in_view_model = ViewModel(cards)

    #assert
    assert len(cards) == 6
    assert items_in_view_model.items == cards

def test_view_model_handles_done_items_correctly(test_cards):
    #arrange
    cards = [card for card in test_cards if card['status']=="done"] 
    
    #act
    items_in_view_model = ViewModel(cards)

    #assert
    assert len(cards) == 1
    assert items_in_view_model.done_items == cards

def test_view_model_handles_todo_items_correctly(test_cards):
    #arrange
    cards = [card for card in test_cards if card['status']=="doing"] 
    
    #act
    items_in_view_model = ViewModel(cards)

    #assert
    assert len(cards) == 2
    assert items_in_view_model.doing_items == cards

def test_view_model_handles_todo_items_correctly(test_cards):
    #arrange
    cards = [card for card in test_cards if card['status']=="doing"] 
    
    #act
    items_in_view_model = ViewModel(cards)

    #assert
    assert len(cards) == 3
    assert items_in_view_model.doing_items == cards