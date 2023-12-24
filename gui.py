import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme('DarkPurple4')

time_label = sg.Text('', key='clock')
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip='Enter To-Do', key="todo")
add_button = sg.Button('Add')
edit_button = sg.Button('Edit/Change')
complete_button = sg.Button('Complete/Delete')
exit_button = sg.Button('Exit')


todos_field = sg.Listbox(values=functions.get_todos(),
                         key='todos',
                         enable_events=True,
                         size=[45, 10])

window = sg.Window('My To-Do App',
                   [[time_label],
                    [label],
                    [input_box, add_button],
                    [todos_field, edit_button, complete_button],
                    [exit_button,]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
#    print(1, event)
#   print(2, values)
#    print(3, values['todos'])

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo']
            todos.append(new_todo.title() + '\n')

            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit/Change':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'

                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select a To-Do first', font=('Helvetica', 20))

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case 'Complete/Delete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)

                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')

            except IndexError:
                sg.popup('Please select a To-Do first', font=('Helvetica', 20))

        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break

window.close()
