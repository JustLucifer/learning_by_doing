from todo_gui_model import sg, window, tasks
import sys

class ToDo:
    
    def run(self):
        while True:
            event, values = window.read()
            print(event, values)
            if event in ('Exit', sg.WINDOW_CLOSED):
                window.close()
                sys.exit()
            elif event.split(':')[0] == 'Delete':
                if values['-TABLE-']:
                    index = values['-TABLE-'][0]
                    del tasks[index]
                    window['-TABLE-'](tasks)