import streamlit as st #to create webapps, data textbox
import functions

todos=functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]+"\n" #some dictionary that will
    # containt the data the user enters in the input box with key=new_todo
    todos.append(todo)
    functions.write_todos(todos)

todos=functions.get_todos()

st.title("My Todo App") #if put at different row, will appear at different row
st.subheader("This is my todo app.")
st.write("This apps is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

#st.checkbox("Buy grocery") #check box that can click

st.text_input(label="Enter a todo", placeholder="Add a new todo...",
              on_change=add_todo,key="new_todo") #on_change is a call back function
#label is the label for the text box and its a require arguement
#Placeholder is a hint or text inside the text box for user to know what to do

st.session_state