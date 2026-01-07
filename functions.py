FILEPATH = "todos.txt"

def get_todos(filename=FILEPATH):
    """Esempio di docstring , questo testo racchiuso tra 3 apici consiste nella codumentazione di una funzione.
    Per printare la docunmentazione si può fare : help(<nome_funzione>)"""
    with open(filename, 'r') as file:
        todos_local = file.readlines()
        return todos_local
def write_todos(todos_arg, filepath="todos.txt"): # qui mentre la richiamiamo passiamo il file e la roba da scrivere#
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)