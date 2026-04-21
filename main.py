def get_todos(filepath="todos.txt"):
    """
    Read a text file and return the list of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos

def write_todos(todos_arg, filepath="todos.txt"):
    """ Write a to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos("todos.txt")

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos("todos.txt")

        # Interesting way to solve
        new_todos = [f"{index + 1}-{item.strip('\n')}" for index, item in enumerate(todos)]

        for row in new_todos:
            print(row)

        # for index, item in enumerate(todos):
        #     item = item.strip('\n')
        #     row = f"{index + 1}-{item}"
        #     print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos("todos.txt")

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid. Try again.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos("todos.txt")
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} is complete, and remove from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid. Try again.")

print("Bye!")
