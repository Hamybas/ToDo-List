import streamlit as st
import functions

st.title('My To-Do App')

todos = functions.get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input('', placeholder='Add new To-Do')

