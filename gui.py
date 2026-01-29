import functions
import FreeSimpleGUI as sg

#from cli import new_todo

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to do", key='todo',
                         enable_events=True, size=[45, 10])
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
#listbob , il valore di "key" serve ad indetificare univocamente un oggetto!
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])

window = sg.Window('My to-do App', layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))

# associamo alle 2 variabili evento il valore della window , quindi questo conterrà i
# valori dei button che premiamo e del testo che scriviamo

while True:
    event, values = window.read()
    print(1, f"hai premuto il tasto(evento):", {event})
    print(2, f"hai inserito: {values['todo']}")
    print(3, f"hai selezionato: {values['todos']}")
    print(4, values['todos'])

    match event:
        case"Add":
            todos = functions.get_todos()
            ## quel #'todoo' è il rif. all inputbox che è di tipo dizionario, abbimao messo la key=todoo
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            #aggiorniamo in diretta i valori
            window['todos'].update(values=todos)

        case"Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"

            todos = functions.get_todos()
            #la funz. index ci restituisce indice di un dato valore dell'array
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            #facciamo update della listbox indent. dalla key "todos", come value ripassiamo il cont. del file txt
            window['todos'].update(values=todos)
        case 'todos':
            #intercettiamo il click su un elemento della lista (key=todos), quin
            #idem qui aggiorniamo il valore della inputbox con quello che abbiamo selex. nella listbox
            window['todo'].update(value=values['todos'][0])

        #qui intercettiamo il pulsante di chiusura per gestire la chiusura della windod, altrimenti adnrebbe in err..
        case sg.WIN_CLOSED:
            break

    print("byye")
window.close()

