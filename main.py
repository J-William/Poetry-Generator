import PySimpleGUI as sg
from App import App, getAvailableAuthors, getAuthorTitles

# SETUP ================================================================================================================

# An App object will hold the list of selected songs/poems and the current model
app = App()

# Get the list of authors currently available on poet-db
authors_list = getAvailableAuthors()


# LAYOUT ===============================================================================================================
sg.theme('BluePurple')



buttons_column = [
        [sg.Button('Add', size=(8,2), key='addTitle')],
        [sg.Button('Remove', size=(8,2), key='removeTitle')]
]

lower_right_column = [
    [sg.T('Choose different combinations of poems ')],
    [sg.T('with the shuttle buttons to use as models')],
    [sg.T('for generating new text.')]
#    [sg.Push(), sg.vbottom(sg.Button('Generate Poem', key='generatePoem'))]
]

# main layout
layout = [
    # Row 1
    [
        sg.Listbox(authors_list, size=(30, 15), enable_events=True, key='authorChoice'),
        sg.Listbox([], size=(50, 15), key='poemChoice', select_mode="multiple"),
        sg.Column(buttons_column, element_justification='center'),
        sg.Listbox([], size=(75, 15), key='modelItems')
    ],
    # Row 2
    [
        sg.Multiline(size=(84, 20), key='poemOutput'),
        sg.Push(), sg.Column(lower_right_column, element_justification='left'),
        sg.Push(), sg.vbottom(sg.Button('Generate Poem', key='generatePoem'))
    ]
]

window = sg.Window('Poetry Generator', layout, size=(1200, 500))

# EVENT LOOP ===========================================================================================================
while True:  # Event Loop
    event, values = window.read()
    print(event, values)

    # Exit application
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    # Author changed in poetry tab
    if event == 'authorChoice':
        author = values['authorChoice'][0]
        titles = getAuthorTitles(author)

        poem_list = [e['title'] for e in titles]
        window['poemChoice'].update(poem_list)

    # Poem added to training list
    if event == 'addTitle':
        # Parse state values
        author = values['authorChoice'][0]
        titles = values['poemChoice']
        # Add any new selections
        titles.extend(app.poems.get(author, []))
        app.poems[author] = titles
        # Flush the old model anytime training list is changed
        app.model = None

    # Generate a poem
    if event == 'generatePoem':
        newPoem = app.generatePoem(10)
        window['poemOutput'].update(newPoem)

    # Update the training list
    window['modelItems'].update(app.listItems())


print('----Memory Dump----')
print('Poems: ', app.poems)
print('Songs: ', app.songs)

window.close()
