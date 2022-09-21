from todo_gui_model import sg, window
import sys

class ToDo:
    
    def run(self):
        while True:
            event, values = window.read()
            print(event, values)
            if event in ('Exit', sg.WINDOW_CLOSED):
                window.close()
                sys.exit()