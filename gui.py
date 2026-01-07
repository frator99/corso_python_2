import functions
import FreeSimpleGUI as sg

#from cli import new_todo

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to do", key='todo')
add_button = sg.Button("Add")

window = sg.Window('My to-do App', layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

# associamo alle 2 variabili evento il valore della window , quindi questo conterrà i
# valori dei button che premiamo e del testo che scriviamo

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case"Add":
            todos = functions.get_todos()
            ## quel #'todoo' è il rif. all inputbox che è di tipo dizionario, abbimao messo la key=todoo
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        #qui intercettiamo il pulsante di chiusura per gestire la chiusura della windod, altrimenti adnrebbe in err..
        case sg.WIN_CLOSED:
            break

        #case"Edit"
    print("byye")
window.close()

