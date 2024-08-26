from pywebio import start_server
from pywebio.input import input, input_group
from pywebio.output import put_text, put_table, put_buttons, use_scope, clear, put_html, put_scope
from pywebio.session import set_env

tasks = []


def main():
    set_env(title="Task Manager")

    put_html("<h1 style='text-align: center;'>Task Manager</h1>")

    # Create scopes for different sections
    put_scope("task_input")
    put_scope("task_list")
    put_scope("task_details")

    update_task_input()
    update_task_list()


def update_task_input():
    with use_scope('task_input', clear=True):
        put_html("<h2>Add New Task</h2>")
        data = input_group("New Task", [
            input("Task Name", name="name", required=True),
            input("Description", name="description")
        ])
        tasks.append(data)
        update_task_list()


def update_task_list():
    with use_scope('task_list', clear=True):
        put_html("<h2>Task List</h2>")
        if not tasks:
            put_text("No tasks yet.")
        else:
            put_table([
                ["Task", "Actions"],
                *[[task['name'],
                   put_buttons(['View', 'Delete'],
                               onclick=[
                                   lambda t=task: view_task(t),
                                   lambda i=i: delete_task(i)
                               ])
                   ] for i, task in enumerate(tasks)]
            ])


def view_task(task):
    with use_scope('task_details', clear=True):
        put_html("<h2>Task Details</h2>")
        put_text(f"Name: {task['name']}")
        put_text(f"Description: {task['description']}")


def delete_task(index):
    tasks.pop(index)
    update_task_list()
    clear('task_details')


if __name__ == '__main__':
    start_server(main, port=8080)
