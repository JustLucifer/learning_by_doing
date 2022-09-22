import PySimpleGUI as sg

tasks = [['2022-09-22', 'buy milk'], ['2022-09-22', 'buy shoes'], ['2022-09-23', 'feed cat']]

frame = [
    [sg.Table(values=tasks, headings=['Date', 'Tasks'], k='-TABLE-',
              num_rows=21, auto_size_columns=False, hide_vertical_scroll=True,
              row_height=30, font='None 15', enable_click_events = True,
              col_widths=[10,25], justification='l', border_width=0)],
]
layout = [
    [sg.Frame('To Do', frame)],
    [sg.B('Add', s=(5,1), border_width=0)]
]

window = sg.Window('ToDo', layout, finalize=True, element_justification='c',
                   font='bold', size=(525, 740), return_keyboard_events=True)
