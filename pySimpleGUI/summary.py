import PySimpleGUI as sg

sg.theme('Reddit')

# -------- Popups ----------
# res = sg.popup_get_text('Please, enter a text:',
#                         # password_char='*',
#                         title='popup',
#                         keep_on_top=True,
#                         location=(800, 375),
#                         font='Courier 18')
# print(res)


# -------- Buttons ----------
# menu_button = ['Menu', ['File', 'Edit', 'View', 'Settings', ['audio', 'graphics']]]


# layout = [
#     [sg.ButtonMenu('Menu', menu_def=menu_button)],
#     [sg.B('Button 1'), sg.B('Button 2')],
#     [sg.Ok(tooltip='Submit'), sg.Cancel(button_color='red')]
# ]

# window = sg.Window('Buttons', layout)
# event, values = window.read()
# print(event, values)


# ----------- CheckBox & DropDown -------------

# languages = ['English', 'German', 'French']

# col_1 = [
#     [sg.T('What is your name:')],
#     [sg.I(key='-NAME-', size=(16, 10))],
#     [sg.Ok(), sg.Cancel()],
# ]

# col_2 = [
#     [sg.CB('python', key='-python-')],
#     [sg.CB('C#', key='-C#-')],
#     [sg.CB('php', key='-php-')],
#     [sg.DD(languages, key='-LANGUAGE-', default_value=languages[0])],
# ]

# layout = [
#     [sg.Col(col_1), sg.VerticalSeparator(), sg.Col(col_2)],
# ]

# window = sg.Window('My App', layout)

# while True:
#     event, values = window.read()
#     if event == 'Cancel':
#         window.close()
#         break
#     elif event == 'Ok':
#         sg.popup('Your name is', values['-NAME-'])
#     print(event, values)


# ----------- Frame Listbox Menu Multiline -----------------

# cities = ['Paris', 'Berlin', 'London', 'Kiev', 'Helsinki', 'New-York']
# menu = [
#     ['File', ['New file', 'Open', 'Save', 'Exit']],
#     ['Edit', ['Copy', 'Past']],
#     ['Help', ['Tutorials', 'About']],
# ]

# frame = [
#     [sg.T('Name:'), sg.I(key='-NAME-')],
#     [sg.HorizontalSeparator()],
#     [sg.CB('Python', key='-python-'), sg.CB('C#', key='-C#-')],
#     [sg.LB(cities, size=(8,4), key='city')], # result as list
# ]

# layout = [
#     [sg.Menu(menu, key='-MENU-')],
#     [sg.Multiline(key='-MULTI-', size=(53, 5))],
#     [sg.Frame('My Frame', frame)],
#     [sg.Ok(), sg.Cancel()],
# ]

# window = sg.Window('My App', layout,)

# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event in ['Cancel', 'Exit']:
#         window.close()
#         break
#     print(event, values)


# ----------- Progress Bar -----------------

# layout = [
#     [sg.ProgressBar(1000, orientation='h', size=(50, 25), key='-PRSBAR-')],
#     [sg.Cancel()]
# ]

# window = sg.Window('My App', layout,)

# for i in range(1000):
#     event, values = window.read(timeout=1)
#     if event == sg.WIN_CLOSED or event == 'Cancel':
#         window.close()
#         break
#     window['-PRSBAR-'].update(i+1)
# print(event, values)
# window.close()


# ------------- Tabs -----------------

tab_1 = [
    [sg.T('Full Name'), sg.I(size=(30,4),)],
    [sg.Ok('Sumbit'), sg.Cancel()],
]

tab_2 = [
    [sg.CB('Python', size=(10,4)), sg.CB('C#',)],
    [sg.CB('JavaScript', size=(10,4)), sg.CB('Java',)],
]

layout = [
    [sg.TabGroup([
        [sg.Tab('Tab 1', tab_1), sg.Tab('Tab 2', tab_2)]
    ])]
]

window = sg.Window('My App', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        window.close()
        break
    print(event, values)