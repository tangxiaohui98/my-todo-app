FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH): #something like function block, can include variable that would like the user to enter everytime they call this function
    """Read a text file and return the list of to-do list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines() #variable inside def block will be local variable, outside will be gloobal
    return todos_local #return todos to get_todos, when dont have this return statement, will return none


def write_todos(todos_arg,filepath=FILEPATH): #this function do not return variable, but to do some task when being called
    """Read a text file and return the list of 
    to-do items.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

#__name__ record the name of the modules currently running

def parse(feet_inches): #will return as tuple
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return{"feet":feet, "inches":inches} #when to call feet and inches, need to call the variable [feet]


def convert(feet,inches):
    meters=feet*0.3048+inches*0.0254
    return meters