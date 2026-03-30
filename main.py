while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

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

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid. Try again.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

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
