class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.tasks.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_list = [task for task in self.tasks if task.complete == False]
        return incomplete_list

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_list = [task for task in self.tasks if task.complete == True]
        return complete_list


    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for task in self.tasks:
            task.complete = True

