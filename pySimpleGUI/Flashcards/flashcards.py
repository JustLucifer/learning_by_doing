import PySimpleGUI as sg
from time import sleep


class FlashcardsApp:

    def __init__(self) -> None:
        sg.theme('DarkGrey13')

    def create_start_window(self):
        layout = [
            [sg.T('', s=(1,19))],
            [sg.Button('Start learning', f='Arial 20', s=(20,2), p=0)],
            [sg.T('')],
            [sg.Button('Quit', f='Arial 20', s=(20,2), p=0)],
        ]

        return sg.Window('Flashcards', layout, size=(400,700), element_justification='c')

    def create_main_window(self):
        layout = [
            [sg.ProgressBar(10000, s=(50, 5), k='-PROGRESS-')],
            [sg.Text('some card', s=(10,1), f='Arial 20', p=((0,0),(175,100)), auto_size_text=True)],
            [sg.Text('translate', s=(10,1), f='Arial 20', p=((0,0),(100,175)), auto_size_text=True)],
            [sg.Button('Wrong', p=0, s=(9, 2)), sg.Text(' '*7), 
             sg.Button('See card', p=0, s=(9, 2)), sg.Text(' '*7), 
             sg.Button('Right', p=0, s=(9, 2))]
        ]
        
        return sg.Window('Flashcards', layout, size=(400,700), finalize=True,
                         element_justification='c', text_justification='c',)

    def progress_bar_update(self):
        for i in range(10000):
            i += 1
            sleep(1)
        return i

    THREAD_KEY = '-THREAD-'
    DL_START_KEY = '-START DOWNLOAD-'
    DL_COUNT_KEY = '-COUNT-'
    DL_THREAD_EXITNG = '-THREAD EXITING-'

    def the_thread(self, window:sg.Window):
        max_value = 30
        window.write_event_value((self.THREAD_KEY, self.DL_START_KEY), max_value)
        for i in range(max_value):
            sleep(.1)
            window.write_event_value((self.THREAD_KEY, self.DL_COUNT_KEY), i)

    def mainloop(self):
        window = self.create_main_window()
        window['-PROGRESS-'](1)
        window.start_thread(lambda: self.the_thread(window), (self.THREAD_KEY, self.DL_THREAD_EXITNG))
        while True:
            self.event, values = window()
            if self.event == sg.WIN_CLOSED:
                window.close()
                break
            elif self.event in ('Right', 'Wrong'):
                window.start_thread(lambda: self.the_thread(window), (self.THREAD_KEY, self.DL_THREAD_EXITNG))
            # Events coming from the Thread
            elif self.event[0] == self.THREAD_KEY:
                if self.event[1] == self.DL_START_KEY:
                    max_value = values[self.event]
                    window['-PROGRESS-'].update(0, max_value)
                elif self.event[1] == self.DL_COUNT_KEY:
                    window['-PROGRESS-'].update(values[self.event]+1, max_value)

    def run(self):
        start_window = self.create_start_window()
        self.event = start_window()
        while True:
            if self.event[0] in ('Quit', sg.WIN_CLOSED):
                start_window.close()
                break
            elif self.event[0] == 'Start learning':
                start_window.close()
                self.mainloop()
                break
