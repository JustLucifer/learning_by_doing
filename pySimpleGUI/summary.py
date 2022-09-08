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

# -----------First App -------------

languages = ['English', 'German', 'French']

col_1 = [
    [sg.T('What is your name:')],
    [sg.I(key='-NAME-', size=(16, 10))],
    [sg.Ok(), sg.Cancel()],
]

col_2 = [
    [sg.CB('python', key='-python-')],
    [sg.CB('C#', key='-C#-')],
    [sg.CB('php', key='-php-')],
    [sg.DD(languages, key='-LANGUAGE-', default_value=languages[0])],
]

layout = [
    [sg.Col(col_1), sg.VerticalSeparator(), sg.Col(col_2)],
]

window = sg.Window('My App', layout)

while True:
    event, values = window.read()
    if event == 'Cancel':
        window.close()
        break
    elif event == 'Ok':
        sg.popup('Your name is', values['-NAME-'])
    print(event, values)
