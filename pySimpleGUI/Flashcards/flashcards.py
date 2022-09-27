import PySimpleGUI as sg
from time import sleep

cards = {
    'Kiev': 'Ukraine',
    'Paris': 'France',
    'Berlin': 'German',
}

class FlashcardsApp:

    def __init__(self) -> None:
        sg.theme('DarkGrey13')

    def create_starting_window(self):
        layout = [
            [sg.T('', s=(1,19))],
            [sg.Button('Start learning', s=(20,2), p=0)],
            [sg.T('')],
            [sg.Button('Quit', s=(20,2), p=0)],
        ]

        return sg.Window('Flashcards', layout, size=(400,700), element_justification='c')

    def create_main_window(self):
        layout = [
            [sg.ProgressBar(10000, s=(50, 5), k='-PROGRESS-')],
            [sg.Text('', s=(10,1), f='Arial 20', p=((0,0),(175,100)), auto_size_text=True, k='-Q-')],
            [sg.Text('', s=(10,1), f='Arial 20', p=((0,0),(100,175)), auto_size_text=True, k='-A-')],
            [sg.Button('Wrong', p=0, s=(9, 2)), sg.Text(' '*7), 
             sg.Button('See card', p=0, s=(9, 2)), sg.Text(' '*7), 
             sg.Button('Right', p=0, s=(9, 2))]
        ]
        
        return sg.Window('Flashcards', layout, size=(400,700), finalize=True,
                         element_justification='c', text_justification='c',)

    THREAD_KEY = '-THREAD-'
    DL_START_KEY = '-START DOWNLOAD-'
    DL_COUNT_KEY = '-COUNT-'
    DL_THREAD_EXITNG = '-THREAD EXITING-'

    def the_thread(self, window:sg.Window):
        max_value = 20
        window.write_event_value((self.THREAD_KEY, self.DL_START_KEY), max_value)
        for i in range(max_value):
            sleep(.1)
            window.write_event_value((self.THREAD_KEY, self.DL_COUNT_KEY), i)

    def mainloop(self):
        i = 0
        window = self.create_main_window()
        question = list(cards)[i]
        answer = list(cards.values())[i]
        window['-Q-'](question)
        window.start_thread(lambda: self.the_thread(window), (self.THREAD_KEY, self.DL_THREAD_EXITNG))

        while True:
            event, values = window()
            if event == sg.WIN_CLOSED:
                window.close()
                break
            elif event == 'See card':
                window['-A-'](answer)
            elif event in ('Right', 'Wrong'):
                window['-A-']('')
                i += 1
                try:
                    question = list(cards)[i]
                    answer = list(cards.values())[i]
                except IndexError:
                    return
                window['-Q-'](question)
                print(question, answer)
                window.start_thread(lambda: self.the_thread(window), (self.THREAD_KEY, self.DL_THREAD_EXITNG))
            # Events coming from the Thread
            elif event[0] == self.THREAD_KEY:
                if event[1] == self.DL_START_KEY:
                    max_value = values[event]
                    window['-PROGRESS-'].update(0, max_value)
                elif event[1] == self.DL_COUNT_KEY:
                    window['-PROGRESS-'].update(values[event]+1, max_value)

    def run(self):
        starting_window = self.create_starting_window()
        event = starting_window()
        while True:
            if event[0] == 'Start learning':
                starting_window.close()
                self.mainloop()
                break
            else:
                starting_window.close()
                break
