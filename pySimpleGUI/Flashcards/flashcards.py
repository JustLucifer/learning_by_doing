import PySimpleGUI as sg
from time import sleep
from models import Flashcard, session
import sys

class FlashcardsApp:

    def __init__(self) -> None:
        sg.theme('DarkGrey13')
        self.count = 0
        self.cards = {}

    def create_starting_window(self):
        layout = [
            [sg.Text('', s=(1,16))],
            [sg.Button('Start learning', s=(20,2), font='bold', p=0, border_width=0)],
            [sg.Text('')],
            [sg.Button('Add cards', s=(20,2), font='bold', p=0, border_width=0)],
            [sg.Text('')],
            [sg.Button('Quit', s=(20,2), font='bold', p=0, border_width=0)],
        ]

        return sg.Window('Flashcards', layout, size=(400,700), element_justification='c')

    def create_add_cards_window(self):
        layout = [
            [sg.Text('Enter a question:', font='Arial 20', p=((0,0),(125,50)))],
            [sg.Input('', s=(20, 20), font='Arial 20', p=((0,0),(0,50)), k='-question-')],
            [sg.Text('Enter an answer:', font='Arial 20', p=((0,0),(50,50)))],
            [sg.Input('', s=(20, 20), font='Arial 20', p=((0,0),(0,100)), k='-answer-')],
            [sg.Button('Add card', font='Arial 20', p=0, border_width=0)],
            [sg.T('', k='-CARD-ADDED-', font='Arial 12', p=(0,10))]
        ]

        return sg.Window('Flashcards', layout, size=(400,700), element_justification='c', finalize=True)

    def create_main_window(self):
        layout = [
            [sg.ProgressBar(10000, s=(50, 5), k='-PROGRESS-')],
            [sg.Text('', font='Arial 20', p=((0,0),(175,100)), auto_size_text=True, k='-Q-')],
            [sg.Text('', font='Arial 20', p=((0,0),(100,175)), auto_size_text=True, k='-A-')],
            [sg.Button('Wrong', p=0, s=(9, 2), font='Arial 11', border_width=0), sg.Text(' '*7),
             sg.Button('See card', p=0, s=(9, 2), font='Arial 11', border_width=0), sg.Text(' '*7),
             sg.Button('Right', p=0, s=(9, 2), font='Arial 11', border_width=0)]
        ]
        
        return sg.Window('Flashcards', layout, size=(400,700), finalize=True,
                         element_justification='c', text_justification='c',)

    THREAD_KEY = '-THREAD-'
    DL_START_KEY = '-START DOWNLOAD-'
    DL_COUNT_KEY = '-COUNT-'
    DL_THREAD_EXITNG = '-THREAD EXITING-'

    def the_thread(self):
        max_value = 20
        self.window.write_event_value((self.THREAD_KEY, self.DL_START_KEY), max_value)
        for i in range(max_value):
            sleep(.1)
            self.window.write_event_value((self.THREAD_KEY, self.DL_COUNT_KEY), i)
        else:
            self.window['-A-'](self.answer)
    
    def generate_new_card(self):
        self.window['-A-']('')
        self.count += 1
        try:
            self.question = list(self.cards)[self.count]
            self.answer = list(self.cards.values())[self.count]
        except IndexError:
            self.window.close()
            return True
        self.window['-Q-'](self.question)
        self.window.start_thread(lambda: self.the_thread(), (self.THREAD_KEY, self.DL_THREAD_EXITNG))

    def read_cards_from_db(self):
        self.all_cards = session.query(Flashcard).all()
        for i in self.all_cards:
            self.cards[i.question] = i.answer

    def mainloop(self):
        self.window = self.create_main_window()
        self.question = list(self.cards)[0]
        self.answer = list(self.cards.values())[0]
        self.window['-Q-'](self.question)
        self.window.start_thread(lambda: self.the_thread(), (self.THREAD_KEY, self.DL_THREAD_EXITNG))

        while True:
            event, values = self.window()
            if event == sg.WIN_CLOSED:
                self.window.close()
                break
            elif event == 'See card':
                self.window['-A-'](self.answer)
            elif event in ('Right', 'Wrong'):
                if self.generate_new_card():
                    self.count = 0
                    break
            # Events coming from the Thread
            elif event[0] == self.THREAD_KEY:
                if event[1] == self.DL_START_KEY:
                    max_value = values[event]
                    self.window['-PROGRESS-'].update(0, max_value)
                elif event[1] == self.DL_COUNT_KEY:
                    self.window['-PROGRESS-'].update(values[event]+1, max_value)
    
    def add_cards_menu(self):
        window = self.create_add_cards_window()
        while True:
            event, values = window()
            if values is not None:
                q = values['-question-']
                a = values['-answer-']

            if event == sg.WIN_CLOSED:
                window.close()
                break
            elif event == 'Add card' and q != '' and a != '':
                window['-question-']('')
                window['-answer-']('')
                window['-CARD-ADDED-']('Card Created')
                session.add(Flashcard(question=q, answer=a))
                session.commit()

    def run(self):
        while True:
            starting_window = self.create_starting_window()
            event = starting_window()
            if event[0] == 'Start learning':
                starting_window.close()
                self.mainloop()
            elif event[0] == 'Add cards':
                starting_window.close()
                self.add_cards_menu()
            else:
                starting_window.close()
                session.close()
                sys.exit()