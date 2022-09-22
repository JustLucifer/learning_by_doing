import PySimpleGUI as sg
from models import session, Task

theme = sg.theme('LightBlue2')

tasks = session.query(Task).order_by(Task.date)
tasks = [[task.date, task.task] for task in tasks]

frame = [
    [sg.Table(values=tasks, headings=['Date', 'Tasks'], k='-TABLE-',
              num_rows=21, auto_size_columns=False, hide_vertical_scroll=True,
              row_height=30, font='None 15', enable_click_events = True,
              col_widths=[10,25], justification='l', border_width=0)],
]

layout = [
    [sg.Frame('To Do', frame, p=5)],
    [sg.B('History', s=(6,1), border_width=0, p=0),
     sg.T('    '),
     sg.B('Add', s=(6,1), border_width=0, p=0),
     sg.T('    '),
     sg.B('Exit', s=(6,1), border_width=0, p=0)]
]

window = sg.Window('ToDo', layout, finalize=True, element_justification='c',
                   font='bold', size=(525, 735), return_keyboard_events=True)
