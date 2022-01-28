import PySimpleGUI as sg
from poetpy import get_poetry


sg.theme('BluePurple')

# Get the list of authors currently available on poetdb
authors_list = list(get_poetry('author')['authors'])

poem_list = []
poem = ""

poetry_layout = [
                    [sg.T('Pick an author to include. ')],
                    [sg.Listbox(authors_list, size=(25, 8)), sg.Listbox(poem_list, size=(25, 8))]
                ]

lyrics_layout = [
                    [sg.T('Search for an artist.')],
                    [sg.In(key='in')]
                ]

layout = [
    [sg.TabGroup([[sg.Tab('Poetry', poetry_layout), sg.Tab('Lyrics', lyrics_layout)]], size=(550, 200)), sg.Listbox(['sup', 'howdy', 'yo'], size=(25, 10))],
    [sg.Multiline(poem, size=(76, 200)), sg.Push(), sg.vbottom(sg.Button('Generate Poem'))]
]


window = sg.Window('Poetry Generator', layout, size=(800, 400))

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        # window['-OUTPUT-'].update(values['-IN-'])
        pass

window.close()

# layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]])],
#               [sg.Button('Read')]]
