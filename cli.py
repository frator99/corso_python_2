#from functions import get_todos, write todos   metodo alternativo per importare le funzioni.

import functions
import time

#todos =  []
now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)
while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add") :
        todo = user_action[4:] + '\n'
        todos = functions.get_todos()

        todos.append(todo)
        functions.write_todos("todos.txt", todos)


    elif user_action.startswith("show"):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1 }--{item}")


    elif user_action.startswith("edit"):
        number = int(user_action[5:])
        number = number -1
        todos = functions.get_todos()
        new_todo = input("Enter new todo task: ")

        todos[number] = new_todo + '\n' # asssegnamo il nuovo valore all'elemento della list
        functions.write_todos("todos.txt", todos)
    elif user_action.startswith("complete"):
        number = int(user_action[9:])
        todos = functions.get_todos()
        index = number -1
        todo_to_remove = todos[index].strip('\n')#storiamo va. da elim.
        todos.pop(number -1)  #eliminiamo il val. da array
        functions.write_todos("todos.txt", todos)
        message = f"Todo '{todo_to_remove}' was removed from list"
        print(message)
    elif user_action.startswith("exit"):
        print("++++ esco dallo script ++++")
        break
    else:
        print("Please insert right command!!!")
print("Bye!")