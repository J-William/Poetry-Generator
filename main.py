import PySimpleGUI as sg


sg.theme('BluePurple')


poem = ""

# layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
#           [sg.Input(key='-IN-')],
#           [sg.Button('Show'), sg.Button('Exit')]]

tab1_layout = [[sg.T('This is inside tab 1')]]

tab2_layout = [[sg.T('This is inside tab 2')],
               [sg.In(key='in')]]

col1 = []



layout = [
            [sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]], size=(400, 200)), sg.Listbox(['sup', 'howdy', 'yo'], size=(200, 10))],
            [sg.Multiline(poem, size=(75, 200)), sg.Button('Generate Poem')]
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
