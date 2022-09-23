import PySimpleGUI as sg
from models import session, Task, History
from datetime import datetime
import sys

class ToDo:
    sg.theme('LightBlue2')

    def __init__(self) -> None:
        self.db_tasks = session.query(Task).order_by(Task.date).order_by(Task.priority)
        self.window = self.create_main_window()
        self.priorities = ('P1', 'P2', 'P3', 'P4')

    def choose_color_for_rows(self) -> list:
        """Chose color according to priority of task"""
        lst_of_colors = []
        for n, task in enumerate(self.db_tasks):
            color = ''
            if task.priority == 'P1':
                color = '#e1a2e4'
            elif task.priority == 'P2':
                color = '#b5b151'
            elif task.priority == 'P3':
                color = '#78b5df'
            lst_of_colors.append((n, color))
        return lst_of_colors

    def create_main_window(self):
        self.tasks = [[task.date, task.task] for task in self.db_tasks]

        frame = [
            [sg.Table(values=self.tasks, headings=['Date', 'Tasks'], k='-TABLE-',
                    num_rows=21, auto_size_columns=False, hide_vertical_scroll=True,
                    row_height=30, font='None 15', enable_click_events = True,
                    col_widths=[10,25], justification='l', border_width=0,
                    row_colors = self.choose_color_for_rows(),)],
        ]

        layout = [
            [sg.Frame('To Do', frame, p=5)],
            [sg.B('History', s=(6,1), border_width=0, p=0),
            sg.T('    '),
            sg.B('Add', s=(6,1), border_width=0, p=0),
            sg.T('    '),
            sg.B('Exit', s=(6,1), border_width=0, p=0)]
        ]

        return sg.Window('ToDo', layout, finalize=True, element_justification='c',
                                font='bold', size=(525, 735), return_keyboard_events=True)

    def update_window_table(self):
        self.tasks = session.query(Task).order_by(Task.date).order_by(Task.priority)
        self.tasks = [[task.date, task.task] for task in self.tasks]
        self.window['-TABLE-'](self.tasks, row_colors=self.choose_color_for_rows())

    def get_today_date(self):
        today_date = datetime.today()
        today_date_str = today_date.strftime('%Y-%m-%d')
        return today_date_str

    def create_add_window2(self):
        layout2 = [
            [sg.I(s=(15,2), font=(None,25), k='-TASK-')],
            [sg.CalendarButton('Set date', font='bold', target='-DATE-'),
            sg.T(self.get_today_date(), font='bold', k='-DATE-'),
            sg.Combo(self.priorities, default_value='priority', s=(7,1), font='bold', k='-PRIORITY-')],
            [sg.Ok(font='bold'), sg.Cancel(font='bold')],
        ]

        return sg.Window('Add task', layout2, finalize=True)

    def add_task(self, window2, values2):
        if values2['-TASK-']:
            priority = values2['-PRIORITY-'] if values2['-PRIORITY-'] != 'priority' else 'P4'
            date = datetime.strptime(window2['-DATE-'].get(), '%Y-%m-%d')
            session.add(Task(date=date, task=values2['-TASK-'], priority=priority))
            window2.close()
            self.update_window_table()

    def show_add_task_window(self):
        window2 = self.create_add_window2()
        while True:
            event2, values2 = window2.read()
            if event2 == 'Ok':
                self.add_task(window2, values2)
            else:
                window2.close()
                break

    def delete_task(self, index):
        session.delete(session.query(Task).filter(Task.task == self.cur_task).first())
        del self.tasks[index]
        self.window['-TABLE-'](self.tasks)

    def edit_task(self, window3, values3):
        new_date = datetime.strptime(window3['-DATE-'].get(), '%Y-%m-%d').date()
        edit_t = session.query(Task).filter(Task.task == self.cur_task).first()
        edit_t.task = values3['-TASK-']
        edit_t.date = new_date
        edit_t.priority = values3['-PRIORITY-']
        self.update_window_table()

    def show_edit_task_window(self, index):
        if index in (-1, None):
            return
        date, self.cur_task = self.tasks[index][0], self.tasks[index][1]
        done_task = session.query(Task).filter(Task.task == self.cur_task).first()
        layout3 = [
            [sg.I(default_text = self.cur_task, s=(15,2), font=(None,25), k='-TASK-')],
            [sg.CalendarButton('Set date', font='bold', target='-DATE-'), sg.T(date, font='bold', k='-DATE-'),
             sg.Combo(self.priorities, default_value=done_task.priority, s=(7,1), font='bold', k='-PRIORITY-')],
            [sg.Ok(font='bold'), sg.B('Done',font='bold'), sg.B('Delete',font='bold')],
        ]

        window3 = sg.Window('Edit task', layout3, finalize=True)

        while True:
            event3, values3 = window3.read()
            if event3 == 'Delete':
                self.delete_task(index)
            elif event3 == 'Done':
                session.add(History(date=done_task.date, task=done_task.task))
                self.delete_task(index)
            elif event3 == 'Ok':
                if values3['-TASK-']:
                    self.edit_task(window3, values3)
            window3.close()
            break

    def create_history_window4(self):
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

    def show_history(self):
        window4 = self.create_history_window4()
        while True:
            self.window.hide()
            event4, values4 = window4.read()
            if event4 in ('Back', sg.WIN_CLOSED):
                window4.close()
                self.window.un_hide()
                break
            elif event4 == 'Exit':
                window4.close()
                self.close_all()

    def close_all(self):
        self.window.close()
        session.commit()
        session.close()
        sys.exit()

    def run(self):
        while True:
            event, values = self.window.read()
            print(event, values)
            if event in ('Exit', sg.WIN_CLOSED):
                self.close_all()
            elif event == 'Add':
                self.show_add_task_window()
            elif event[0] == '-TABLE-':
                self.show_edit_task_window(index=event[2][0])
            elif event == 'History':
                self.show_history()
