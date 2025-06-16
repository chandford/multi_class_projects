from lib.todo import Todo
from lib.todo_list import TodoList


def test_todo_properties():
    to_do = Todo("laundry")
    assert to_do.task == "laundry"
    assert to_do.complete == False

def test_mark_complete():
    to_do = Todo("baking")
    to_do.mark_complete()
    assert to_do.complete == True


