import PySimpleGUI as sg
from PySimpleGUI import B

sg.theme('DarkBrown4')

col = [
    [B('7', s=(3,2)), B('8', s=(3,2)), B('9', s=(3,2))],
    [B('4', s=(3,2)), B('5', s=(3,2)), B('6', s=(3,2))],
    [B('1', s=(3,2)), B('2', s=(3,2)), B('3', s=(3,2))],
    [B(u'\u221A', s=(3,2), k='-SQRT-'), B('0', s=(3,2)), B('.', s=(3,2), k='-DOT-')],
]

col_1 = [
    [B('*', s=(3,2), k='*')],
    [B('-', s=(3,2), k='-')],
    [B('+', s=(3,5), k='+')],
]

col_2 = [
    [B('/', s=(3,2), k='/')],
    [B('C', s=(3,2), k='-CLEAR-')],
    [B('CE', s=(3,2), k='-CLEAR_EVR-')],
    [B('=', s=(3,2), k='-EQUAL-', button_color='#b30059')],
]

layout = [
    [sg.I(font=(None, 28), s=(14,1), k='-INPUT-',
          background_color='#ffb380', text_color='#000000',)],
    [sg.T(k='-ERROR_OUT-', s=(None,1), p=0, text_color='#faf9f3')],
    [sg.Col(col, p=0), sg.VerticalSeparator(color='#ffb380'),
     sg.Col(col_1, p=0), sg.Col(col_2, p=0)],
]

window = sg.Window('Simple Calculator', layout, font='bold')