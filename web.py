import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")
#test
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My todo app")
st.subheader("Subheader test")
st.write("This is web app for todo")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="input_label", label_visibility="hidden", placeholder="Enter a todo ...",
              on_change=add_todo, key='new_todo')
print("Hello from subsite web.py")

# obiekt, który zwiera wpisane dane w aplikacji test2
st.session_state