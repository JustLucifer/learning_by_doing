import PySimpleGUI as sg

sg.theme('LightBlue')

class TicTacToe:
    
    NUMS = [i for i in range(9)]
    
    def __init__(self) -> None:
        self.turn = 'first'
        self.cells = ['' for _ in range(9)]
        self.layout = [[sg.T('Player 1', font='Arial 15'), sg.T(text=' ' * 47), sg.T('Player 2', font='Arial 15'),],
                  [sg.T(text=' ' * 3), sg.T(0, font='bold'), sg.T(text=' ' * 63), sg.T(0, font='bold')],
                  [sg.B(self.cells[0], s=(10,8), font='bold', p=0, k='0', border_width=3), 
                   sg.B(self.cells[1], s=(10,8), font='bold', p=0, k='1', border_width=3),
                   sg.B(self.cells[2], s=(10,8), font='bold', p=0, k='2', border_width=3)],
                  [sg.B(self.cells[3], s=(10,8), font='bold', p=0, k='3', border_width=3), 
                   sg.B(self.cells[4], s=(10,8), font='bold', p=0, k='4', border_width=3),
                   sg.B(self.cells[5], s=(10,8), font='bold', p=0, k='5', border_width=3)],
                  [sg.B(self.cells[6], s=(10,8), font='bold', p=0, k='6', border_width=3), 
                   sg.B(self.cells[7], s=(10,8), font='bold', p=0, k='7', border_width=3),
                   sg.B(self.cells[8], s=(10,8), font='bold', p=0, k='8', border_width=3)]
        ]
        
        self.window = sg.Window('TicTacToe', self.layout)
    
    def run(self) -> None:
        while True:
            event, values = self.window.read()
            print(event, values)
            if event == sg.WIN_CLOSED:
                self.window.close()
                break
            elif int(event) in self.NUMS:
                if self.cells[int(event)] == '':
                    if self.turn == 'first':
                        self.cells[int(event)] = 'X'
                        self.turn = 'second'
                        self.window[event]('X')
                    elif self.turn == 'second':
                        self.cells[int(event)] = 'O'
                        self.window[event]('O')
                        self.turn = 'first'
