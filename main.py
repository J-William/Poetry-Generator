import PySimpleGUI as sg
from App import App, getAvailableAuthors, getAuthorTitles

# SETUP ================================================================================================================

# An App object will hold the list of selected songs/poems and the current model
app = App()

# Get the list of authors currently available on poet-db
authors_list = getAvailableAuthors()


# LAYOUT ===============================================================================================================
sg.theme('BluePurple')

# poetry tab sub-layout
poetry_layout = [
    # Row 1 Title
    [sg.T('Pick an author to include. ')],
    # Row 2 Content
    [
        sg.Listbox(authors_list, size=(25, 8), enable_events=True, key='authorChoice'),
        sg.Listbox([], size=(28, 8), key='poemChoice', select_mode="multiple"),
        sg.vbottom(sg.Button('Add', key='addTitle'))
    ]
]

# lyrics tab sub-layout
lyrics_layout = [
    [sg.T('Search for an artist.')],
    [sg.In(key='artistSearch')]
]

# main layout
layout = [
    # Row 1
    [
        sg.TabGroup([[sg.Tab('Poetry', poetry_layout), sg.Tab('Lyrics', lyrics_layout)]], size=(550, 200),
                    key='tabGroup'),
        sg.Listbox([], size=(25, 10), key='modelItems')
    ],
    # Row 2
    [
        sg.Multiline(size=(76, 200), key='poemOutput'), sg.Push(),
        sg.vbottom(sg.Button('Generate Poem', key='generatePoem'))
    ]
]

window = sg.Window('Poetry Generator', layout, size=(800, 400))

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
