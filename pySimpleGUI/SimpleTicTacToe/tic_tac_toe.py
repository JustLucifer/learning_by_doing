import PySimpleGUI as sg

sg.theme('LightGrey3')

class TicTacToe:
    
    NUMS = [i for i in range(9)]
    
    def __init__(self) -> None:
        self.turn = 'first'
        self.cells = ['' for _ in range(9)]
        self.layout = [[sg.T('Player 1', font='Arial 15', text_color='black'), sg.T(text=' ' * 38), sg.T('Player 2', font='Arial 15', text_color='black'),],
                  [sg.T(text=' ' * 3), sg.T(0, font='bold', text_color='#77d6ec'), sg.T(text=' ' * 54), sg.T(0, font='bold', text_color='#eda4a4')],
                  [sg.B(self.cells[0], font='bold', p=0, k='0', border_width=3, 
                   image_filename='pySimpleGUI/SimpleTicTacToe/images/white.png'), 
                   sg.B(self.cells[1], font='bold', p=0, k='1', border_width=3, 
                   image_filename='pySimpleGUI/SimpleTicTacToe/images/white.png'),
                   sg.B(self.cells[2], font='bold', p=0, k='2', border_width=3, 
                   image_filename='pySimpleGUI/SimpleTicTacToe/images/white.png')],
                  [sg.B(self.cells[3], font='bold', p=0, k='3', border_width=3, 
                   image_filename='pySimpleGUI/SimpleTicTacToe/images/white.png'), 
                   sg.B(self.cells[4], font='bold', p=0, k='4', border_width=3, 
                   image_filename='pySimpleGUI/SimpleTicTacToe/images/white.png'),
                   sg.B(self.cells[5], font='bold', p=0, k='5', border_width=3, 
                   image_filename='pySimpleGUI/SimpleTicTacToe/images/white.png')],
                  [sg.B(self.cells[6], font='bold', p=0, k='6', border_width=3, 
                   image_filename='pySimpleGUI/SimpleTicTacToe/images/white.png'), 
                   sg.B(self.cells[7], font='bold', p=0, k='7', border_width=3, 
                   image_filename='pySimpleGUI/SimpleTicTacToe/images/white.png'),
                   sg.B(self.cells[8], font='bold', p=0, k='8', border_width=3, 
                   image_filename='pySimpleGUI/SimpleTicTacToe/images/white.png')]
        ]
        
        self.window = sg.Window('TicTacToe', self.layout, default_button_element_size=(105,105),
                                size=(360,410))
    
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
                        self.window[event](image_filename='pySimpleGUI/SimpleTicTacToe/images/x.png')
                    elif self.turn == 'second':
                        self.cells[int(event)] = 'O'
                        self.window[event](image_filename='pySimpleGUI/SimpleTicTacToe/images/o.png')
                        self.turn = 'first'
