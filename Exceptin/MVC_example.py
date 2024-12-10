class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self,task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks
    
class TaskVeiw:

    @staticmethod
    def display_tasks(tasks):
        print('Your tasks: ')
        for i, task in enumerate(tasks, ):
            print(f'{i}. {task}')

    @staticmethod
    def display_message(message):
        print(message)

class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self, task):
        self.model.add_task(task)
        self.view.display_message(f'Task {task} added!')

    def remove_task(self, task):
        if task in self.model.get_tasks():
            self.model.remove_task(task)
            self.view.display_message(f'Task {task} removed!')
        else:
            self.view.display_message(f'Task {task} not found')

    def show_tasks(self):
        tasks = self.model.get_tasks()
        self.view.display_tasks(tasks)

if __name__ == "__main__":
    model = TaskModel()
    view = TaskVeiw()
    controler = TaskController(model, view)

    controler.add_task("Buy groceries")
    controler.add_task('Read book')
    controler.show_tasks()
    controler.remove_task('Read book')
    controler.show_tasks()