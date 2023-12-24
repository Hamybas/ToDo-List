import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print('It is', now)

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = functions.get_todos()

        todos.append(todo.title()+'\n')

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = functions.get_todos()

        # new_todos = []
        # for item in todos:
            # new_item = item.strip('\n')
            # new_todos.append(new_item)

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index+1}-{item}'
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(f'You want to edit TODO #{number}')
            number = number - 1

            todos = functions.get_todos()

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo.capitalize() + '\n'

            functions.write_txt(todos)

        except ValueError:
            print('Your command is not valid. Please enter "edit" and # of TODO to edit')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            i = number - 1
            removed_todo = todos[i].strip('\n')
            todos.pop(i)

            functions.write_todos(todos)

            message = f'Todo "{removed_todo}" was removed from the list'
            print(message)
        except IndexError:
            print('Your command is not valid. Please enter "complete" and # of TODO to complete')
            continue
        except ValueError:
            print('Your command is not valid. Please enter "complete" and # of TODO to complete')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Command is not valid')

print('Bye')
