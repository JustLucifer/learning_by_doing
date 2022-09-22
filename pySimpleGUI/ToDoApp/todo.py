from todo_gui_model import sg, window, tasks
from datetime import datetime
import sys

class ToDo:

    def get_today_date(self):
        today_date = datetime.today()
        today_date_str = today_date.strftime("%d-%m-%Y")
        return today_date_str

    
    def add_task(self):
        layout2 = [
            [sg.I(s=(15,2), font=(None,25), k='-TASK-')],
            [sg.CalendarButton('Set date', font='bold'), sg.T(self.get_today_date(), font='bold', k='-DATE-')],
            [sg.Ok(font='bold'), sg.Cancel(font='bold')],
        ]

        window2 = sg.Window('Add task', layout2, finalize=True)

        while True:
            event2, values2 = window2.read()
            if event2 == 'Ok':
                if values2['-TASK-']:
                    date = window2['-DATE-'].get()
                    tasks.append([date, values2['-TASK-']])
                    window2.close()
                    window['-TABLE-'](tasks)
                    break
            elif event2 in ('Cancel', sg.WIN_CLOSED):
                window2.close()
                break
    
    def del_task(self, values):
        if values['-TABLE-']:
            index = values['-TABLE-'][0]
            del tasks[index]
            window['-TABLE-'](tasks)

    def edit_task(self, index):
        date, task = tasks[index][0], tasks[index][1]
        layout3 = [
            [sg.I(default_text = task, s=(15,2), font=(None,25), k='-TASK-')],
            [sg.CalendarButton('Set date', font='bold'), sg.T(date, font='bold', k='-DATE-')],
            [sg.B('Done',font='bold'), sg.B('Delete',font='bold')],
        ]

        window3 = sg.Window('Edit task', layout3, finalize=True)

        while True:
            event3, values3 = window3.read()
            if event3 in ('Done', 'Delete'):
                del tasks[index]
                window['-TABLE-'](tasks)
                window3.close()
                break
            elif event3 in ('Cancel', sg.WIN_CLOSED):
                window3.close()
                break

    def run(self):
        while True:
            event, values = window.read()
            print(event, values)
            if event == sg.WIN_CLOSED:
                window.close()
                sys.exit()
            elif event == 'Add':
                self.add_task()
            elif event == 'Delete':
                self.del_task(values=values)
            elif event[0] == '-TABLE-':
                self.edit_task(event[2][0])