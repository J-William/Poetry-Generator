import PySimpleGUI as sg
from poetpy import get_poetry



# Get the list of authors currently available on poetdb
authors_list = list(get_poetry('author')['authors'])

poem_list = []
poem = ""





# LAYOUT ===============================================================================================================
sg.theme('BluePurple')

# poetry tab sublayout
poetry_layout = [
                    # Row 1 Title
                    [sg.T('Pick an author to include. ')],
                    # Row 2 Content
                    [
                        sg.Listbox(authors_list, size=(25, 8), enable_events=True, key='authorChoice'),
                        sg.Listbox(poem_list, size=(25, 8), key='poemChoice')
                    ]
                ]

# lyrics tab sublayout
lyrics_layout = [
                    [sg.T('Search for an artist.')],
                    [sg.In(key='artistSearch')]
                ]

# main layout
layout = [
    # Row 1
    [
        sg.TabGroup([[sg.Tab('Poetry', poetry_layout), sg.Tab('Lyrics', lyrics_layout)]], size=(550, 200), key='tabGroup'),
        sg.Listbox(['sup', 'howdy', 'yo'], size=(25, 10), key='modelItems')
    ],
    # Row 2
    [
        sg.Multiline(poem, size=(76, 200), key='poemOutput'), sg.Push(),
        sg.vbottom(sg.Button('Generate Poem', key='generatePoem'))
    ]
]


window = sg.Window('Poetry Generator', layout, size=(800, 400))


# EVENT LOOP ===========================================================================================================
while True:  # Event Loop
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'authorChoice':
        print('author chosen!', values['authorChoice'])
        result = get_poetry('author', values['authorChoice'][0], 'title')
        poem_list = [e['title'] for e in result]



window.close()

