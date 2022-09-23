import PySimpleGUI as sg
from models import session, Task, History
from datetime import datetime

sg.theme('LightBlue2')


def create_main_window():
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

    return tasks, sg.Window('ToDo', layout, finalize=True, element_justification='c',
                    font='bold', size=(525, 735), return_keyboard_events=True)


def get_today_date():
    today_date = datetime.today()
    today_date_str = today_date.strftime('%Y-%m-%d')
    return today_date_str


def create_add_window2():
    layout2 = [
        [sg.I(s=(15,2), font=(None,25), k='-TASK-')],
        [sg.CalendarButton('Set date', font='bold'), sg.T(get_today_date(), font='bold', k='-DATE-')],
        [sg.Ok(font='bold'), sg.Cancel(font='bold')],
    ]

    return sg.Window('Add task', layout2, finalize=True)


def create_history_window4():
    history = session.query(History).order_by(-History.id)
    history = [[task.date, task.task] for task in history]
    frame = [
        [sg.Table(values=history, headings=['Date', 'Tasks'], k='-HISTORY-TABLE-',
                num_rows=21, auto_size_columns=False, hide_vertical_scroll=True,
                row_height=30, font='None 15', enable_click_events = True,
                col_widths=[10,25], justification='l', border_width=0)],
    ]

    layout = [
        [sg.Frame('History', frame, p=5)],
        [sg.B('Back', s=(6,1), border_width=0, p=0), sg.T('    '),
        sg.B('Exit', s=(6,1), border_width=0, p=0)]
    ]

    return sg.Window('ToDo', layout, finalize=True, element_justification='c',
                    font='bold', size=(525, 735), return_keyboard_events=True)
