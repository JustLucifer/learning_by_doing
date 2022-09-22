import PySimpleGUI as sg

tasks = [['2022-09-22', 'buy milk'], ['2022-09-22', 'buy shoes'], ['2022-09-23', 'feed cat']]

frame = [
    [sg.Table(values=tasks, headings=['Date', 'Tasks'], k='-TABLE-',
              num_rows=21, enable_events=True, auto_size_columns=False,
              hide_vertical_scroll=True, row_height=30,
              col_widths=[10,30], justification='l', font='None 15')],
]
layout = [
    [sg.Frame('To Do', frame)],
    [sg.B('Add', s=(5,1)), sg.T('   '), sg.B('Delete')]
]

window = sg.Window('ToDo', layout, finalize=True, element_justification='c',
                   font='bold', size=(525, 750), return_keyboard_events=True)
