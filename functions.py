def get_txt(filepath='todos.txt'):
    """ Read a text file and return the list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_txt(todos_arg, filepath="todos.txt"):
    """ Overwrite the to-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == '__main__':
    print(get_todos())