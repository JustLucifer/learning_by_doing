from main_todo_gui_model import sg, window, tasks
from models import session, Task, History
from datetime import datetime
import sys

class ToDo:

    def __init__(self) -> None:
        self.tasks = tasks

    def get_today_date(self):
        today_date = datetime.today()
        today_date_str = today_date.strftime('%d-%m-%Y')
        return today_date_str
    
    def add_task(self, window2, values2):
        if values2['-TASK-']:
            date = window2['-DATE-'].get()
            date = datetime.strptime(date, '%d-%m-%Y')
            session.add(Task(date=date, task=values2['-TASK-']))
            session.commit()
            window2.close()
            self.tasks = session.query(Task).order_by(Task.date)
            self.tasks = [[task.date, task.task] for task in self.tasks]
            window['-TABLE-'](self.tasks)

    def create_add_task_window(self):
        layout2 = [
            [sg.I(s=(15,2), font=(None,25), k='-TASK-')],
            [sg.CalendarButton('Set date', font='bold'), sg.T(self.get_today_date(), font='bold', k='-DATE-')],
            [sg.Ok(font='bold'), sg.Cancel(font='bold')],
        ]

        window2 = sg.Window('Add task', layout2, finalize=True)

        while True:
            event2, values2 = window2.read()
            if event2 == 'Ok':
                self.add_task(window2, values2)
                break
            elif event2 in ('Cancel', sg.WIN_CLOSED):
                window2.close()
                break
    
    def delete_task(self, window3, index, task):
        session.delete(session.query(Task).filter(Task.task == task).first())
        session.commit()
        del self.tasks[index]
        window['-TABLE-'](self.tasks)
        window3.close()

    def create_edit_task_window(self, index):
        if index in (-1, None):
            return
        date, task = self.tasks[index][0], self.tasks[index][1]
        layout3 = [
            [sg.I(default_text = task, s=(15,2), font=(None,25), k='-TASK-')],
            [sg.CalendarButton('Set date', font='bold'), sg.T(date, font='bold', k='-DATE-')],
            [sg.B('Done',font='bold'), sg.B('Delete',font='bold')],
        ]

        window3 = sg.Window('Edit task', layout3, finalize=True)

        while True:
            event3, values3 = window3.read()
            if event3 == 'Delete':
                self.delete_task(window3, index, task)
                break
            elif event3 == 'Done':
                done_t = session.query(Task).filter(Task.task == task).first()
                session.add(History(date=done_t.date, task=done_t.task))
                session.commit()
                self.delete_task(window3, index, task)
            elif event3 in ('Cancel', sg.WIN_CLOSED):
                window3.close()
                break
    
    def show_history(self):
        history = session.query(History).order_by(-History.date)
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

        window4 = sg.Window('ToDo', layout, finalize=True, element_justification='c',
                        font='bold', size=(525, 735), return_keyboard_events=True)
        while True:
            window.hide()
            event4, values4 = window4.read()
            if event4 in ('Back', sg.WIN_CLOSED):
                window4.close()
                window.un_hide()
                break
            elif event4 == 'Exit':
                window4.close()
                self.close_all()

    def close_all(self):
        window.close()
        session.close()
        sys.exit()

    def run(self):
        while True:
            event, values = window.read()
            print(event, values)
            if event in ('Exit', sg.WIN_CLOSED):
                self.close_all()
            elif event == 'Add':
                self.create_add_task_window()
            elif event[0] == '-TABLE-':
                self.create_edit_task_window(event[2][0])
            elif event == 'History':
                self.show_history()