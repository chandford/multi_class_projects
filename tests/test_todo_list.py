from lib.todo import Todo
from lib.todo_list import TodoList


def test_add_integration():
    to_do_1 = Todo("laundry")
    to_do_2 = Todo("groceries")
    todo_list = TodoList()
    assert todo_list.tasks == []
    todo_list.add(to_do_1) 
    assert len(todo_list.tasks) == 1
    assert todo_list.tasks[0].task == "laundry"
    todo_list.add(to_do_2) 
    assert isinstance(todo_list.tasks[1], Todo)
    assert todo_list.tasks[1].task == "groceries"


def test_incomplete_integration():
    to_do_1 = Todo("cleaning")
    to_do_2 = Todo("cooking")
    todo_list = TodoList()
    todo_list.add(to_do_1) 
    todo_list.add(to_do_2) 
    assert type(todo_list.incomplete()) == list
    assert isinstance(todo_list.incomplete()[0], Todo)
    assert todo_list.incomplete()[-1].task == "cooking"

def test_complete_integration():
    to_do_1 = Todo("feed dog")
    to_do_2 = Todo("walk cat")
    to_do_3 = Todo("buy pastries")
    todo_list = TodoList()
    todo_list.add(to_do_1) 
    todo_list.add(to_do_2)
    todo_list.add(to_do_3)
    to_do_1.mark_complete()
    to_do_3.mark_complete()
    assert type(todo_list.complete()) == list
    assert isinstance(todo_list.complete()[0], Todo)
    assert todo_list.complete()[0].task == "feed dog"
    assert todo_list.complete()[1].task == "buy pastries"


def test_give_up_integration():
    to_do_1 = Todo("feed dog")
    to_do_2 = Todo("walk cat")
    to_do_3 = Todo("buy pastries")
    todo_list = TodoList()
    todo_list.add(to_do_1) 
    todo_list.add(to_do_2)
    todo_list.add(to_do_3)
    todo_list.give_up()
    assert len(todo_list.complete()) == 3
    assert len(todo_list.incomplete()) == 0





