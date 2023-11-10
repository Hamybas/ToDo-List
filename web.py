import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title('My To-Do App')

todos = functions.get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label='Your New To-Do', placeholder='Add new To-Do',
              on_change=add_todo, key='new_todo')

print('Hello')
