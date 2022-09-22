from todo_gui_model import sg, window, tasks
import sys

class ToDo:
    
    def add_task(self):
        layout2 = [
            [sg.I(s=(20,1), font='bold', k='-TASK-')],
            [sg.CalendarButton('Set date'), sg.T('', k='-DATE-')],
            [sg.Ok(), sg.Cancel()],
        ]

        window2 = sg.Window('Add task', layout2)

        while True:
            event2, values2 = window2.read()
            if event2 == 'Ok':
                date = window2['-DATE-'].get()
                tasks.append([date, values2['-TASK-']])
                window2.close()
                window['-TABLE-'](tasks)
                break
            elif event2 in ('Cancel', sg.WIN_CLOSED):
                window2.close()
                break

    def run(self):
        while True:
            event, values = window.read()
            print(event, values)
            if event in ('Exit', sg.WIN_CLOSED):
                window.close()
                sys.exit()
            elif event == 'Add':
                self.add_task()