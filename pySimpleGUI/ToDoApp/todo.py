from main_todo_gui_model import *
from models import session, Task, History
import sys

class ToDo:

    def __init__(self) -> None:
        self.tasks, self.window = create_main_window()

    def update_window_table(self):
        self.tasks = session.query(Task).order_by(Task.date)
        self.tasks = [[task.date, task.task] for task in self.tasks]
        self.window['-TABLE-'](self.tasks)

    def add_task(self, window2, values2):
        date = datetime.strptime(window2['-DATE-'].get(), '%Y-%m-%d')
        session.add(Task(date=date, task=values2['-TASK-']))
        self.update_window_table()

    def show_add_task_window(self):
        window2 = create_add_window2()
        while True:
            event2, values2 = window2.read()
            if event2 == 'Ok':
                if values2['-TASK-']:
                    self.add_task(window2, values2)
            else:
                window2.close()
                break
    
    def delete_task(self, window3, index, task):
        session.delete(session.query(Task).filter(Task.task == task).first())
        del self.tasks[index]
        self.window['-TABLE-'](self.tasks)
        window3.close()

    def edit_task(self, window3, values3, task):
        new_date = datetime.strptime(window3['-DATE-'].get(), '%Y-%m-%d').date()
        edit_t = session.query(Task).filter(Task.task == task).first()
        edit_t.task = values3['-TASK-']
        edit_t.date = new_date
        window3.close()
        self.update_window_table()

    def show_edit_task_window(self, index):
        if index in (-1, None):
            return
        date, task = self.tasks[index][0], self.tasks[index][1]
        layout3 = [
            [sg.I(default_text = task, s=(15,2), font=(None,25), k='-TASK-')],
            [sg.CalendarButton('Set date', font='bold'), sg.T(date, font='bold', k='-DATE-')],
            [sg.Ok(font='bold'), sg.B('Done',font='bold'), sg.B('Delete',font='bold')],
        ]

        window3 = sg.Window('Edit task', layout3, finalize=True)

        while True:
            event3, values3 = window3.read()
            if event3 == 'Delete':
                self.delete_task(window3, index, task)
            elif event3 == 'Done':
                done_t = session.query(Task).filter(Task.task == task).first()
                session.add(History(date=done_t.date, task=done_t.task))
                self.delete_task(window3, index, task)
            elif event3 == 'Ok':
                if values3['-TASK-']:
                    self.edit_task(window3, values3, task)
            window3.close()
            break
    
    def show_history(self):
        window4 = create_history_window4()
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
                self.show_edit_task_window(event[2][0])
            elif event == 'History':
                self.show_history()
