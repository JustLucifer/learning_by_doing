import PySimpleGUI as sg

sg.theme('DarkBrown4')

col = [
    [sg.B('7', size=(3,2), font='bold'), sg.B('8', size=(3,2), font='bold'), sg.B('9', size=(3,2), font='bold')],
    [sg.B('4', size=(3,2), font='bold'), sg.B('5', size=(3,2), font='bold'), sg.B('6', size=(3,2), font='bold')],
    [sg.B('1', size=(3,2), font='bold'), sg.B('2', size=(3,2), font='bold'), sg.B('3', size=(3,2), font='bold')],
    [sg.B(u'\u221A', size=(3,2), font='bold', key='-SQRT-'), sg.B('0', size=(3,2), font='bold'), 
     sg.B('.', size=(3,2), font='bold', key='-DOT-')],
]

col_1 = [
    [sg.B('*', size=(3,2), font='bold', key='*')],
    [sg.B('-', size=(3,2), font='bold', key='-')],
    [sg.B('+', size=(3,5), font='bold', key='+')],
]

col_2 = [
    [sg.B('/', size=(3,2), font='bold', key='/')],
    [sg.B('C', size=(3,2), font='bold', key='-CLEAR-')],
    [sg.B('CE', size=(3,2), font='bold', key='-CLEAR_EVR-')],
    [sg.B('=', size=(3,2), font='bold', key='-EQUAL-',
          button_color='#b30059')],
]

layout = [
    [sg.I(font=(None, 28), size=(14,1), key='-INPUT-',
          background_color='#ffb380', text_color='#000000')],
    [sg.Col(col, pad=0), sg.VerticalSeparator(color='#ffb380'),
     sg.Col(col_1, pad=0), sg.Col(col_2, pad=0)],
]

window = sg.Window('Calculator', layout)